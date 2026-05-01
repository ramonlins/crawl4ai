"""
Scrape GMGN AI page and its documentation.
  - https://gmgn.ai/ai?chain=sol  (agent API overview)
  - https://docs.gmgn.ai           (API documentation)

Output: gmgn_docs/ directory with one markdown file per page.
"""

import asyncio
import os
import re
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, DomainFilter, URLPatternFilter, FilterChain
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

OUTPUT_DIR = "gmgn_docs"

# JS to dismiss any popups/modals before scraping
DISMISS_POPUPS_JS = """
(function() {
    // Click common close buttons
    const selectors = [
        '[aria-label="Close"]', '[aria-label="close"]',
        '.modal-close', '.close-btn', '.close-button',
        'button[class*="close"]', 'button[class*="Close"]',
        '[data-dismiss="modal"]',
    ];
    for (const sel of selectors) {
        const el = document.querySelector(sel);
        if (el) { el.click(); }
    }
    // Remove overlay elements
    document.querySelectorAll('.modal, .overlay, [class*="modal"], [class*="popup"]').forEach(el => {
        el.style.display = 'none';
    });
})();
"""


def url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    domain = parsed.netloc.replace(".", "_")
    path = parsed.path.strip("/").replace("/", "__") or "index"
    query = parsed.query.replace("=", "_").replace("&", "__").replace("?", "")
    slug = f"{path}__{query}" if query else path
    slug = re.sub(r"[^\w\-.]", "_", slug)
    return f"{domain}__{slug}.md"


async def scrape_page(crawler, url, config):
    result = await crawler.arun(url, config=config)
    return result


async def deep_crawl(crawler, start_url, allowed_domains, url_patterns, label):
    filter_chain = FilterChain(filters=[
        DomainFilter(allowed_domains=allowed_domains),
        URLPatternFilter(patterns=url_patterns),
    ])
    strategy = BFSDeepCrawlStrategy(
        max_depth=5,
        filter_chain=filter_chain,
        include_external=False,
        max_pages=200,
    )
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        deep_crawl_strategy=strategy,
        delay_before_return_html=3.0,
        page_timeout=30000,
        js_code=DISMISS_POPUPS_JS,
        excluded_tags=["nav", "script", "style"],
        remove_overlay_elements=True,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed"),
            options={"ignore_links": False},
        ),
        stream=True,
    )

    count = 0
    print(f"\n[{label}] Starting deep crawl of {start_url}")
    async for result in await crawler.arun(start_url, config=config):
        if not result.success:
            print(f"  FAIL  {result.url} — {result.error_message}")
            continue

        filename = url_to_filename(result.url)
        filepath = os.path.join(OUTPUT_DIR, filename)
        content = (
            result.markdown.fit_markdown
            if result.markdown and result.markdown.fit_markdown
            else (result.markdown.raw_markdown if result.markdown else "")
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Source: {result.url}\n\n")
            f.write(content)

        count += 1
        print(f"  [{count:>3}] {result.url} → {filename}")

    return count


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    browser_config = BrowserConfig(headless=True, verbose=False)

    total = 0
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # 1. Scrape the /ai page (single page, no deep crawl needed — mostly static content)
        print("[gmgn.ai/ai] Scraping agent overview page...")
        ai_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            delay_before_return_html=4.0,
            page_timeout=30000,
            js_code=DISMISS_POPUPS_JS,
            excluded_tags=["nav", "script", "style"],
            remove_overlay_elements=True,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(threshold=0.35, threshold_type="fixed"),
                options={"ignore_links": False},
            ),
        )
        result = await crawler.arun("https://gmgn.ai/ai?chain=sol", config=ai_config)
        if result.success:
            filename = url_to_filename(result.url)
            filepath = os.path.join(OUTPUT_DIR, filename)
            content = (
                result.markdown.fit_markdown
                if result.markdown and result.markdown.fit_markdown
                else result.markdown.raw_markdown
            )
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Source: {result.url}\n\n")
                f.write(content)
            total += 1
            print(f"  [  1] {result.url} → {filename}")
        else:
            print(f"  FAIL {result.error_message}")

        # 2. Deep crawl docs.gmgn.ai
        count = await deep_crawl(
            crawler,
            start_url="https://docs.gmgn.ai",
            allowed_domains=["docs.gmgn.ai"],
            url_patterns=["https://docs.gmgn.ai/*"],
            label="docs.gmgn.ai",
        )
        total += count

    print(f"\nDone. {total} pages saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
