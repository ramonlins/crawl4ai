"""
Scrape all pages from https://pumpportal.fun (Docusaurus docs).
Output: pumpportal_api/ with one markdown file per page.
"""

import asyncio
import os
import re
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, DomainFilter, URLPatternFilter, FilterChain
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

OUTPUT_DIR = "pumpportal_api"
BASE_URL = "https://pumpportal.fun/"


def url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "__") or "index"
    path = re.sub(r"[^\w\-.]", "_", path)
    return f"{path}.md"


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filter_chain = FilterChain(filters=[
        DomainFilter(allowed_domains=["pumpportal.fun"]),
        URLPatternFilter(patterns=["https://pumpportal.fun/*"]),
    ])

    strategy = BFSDeepCrawlStrategy(
        max_depth=5,
        filter_chain=filter_chain,
        include_external=False,
        max_pages=200,
    )

    browser_config = BrowserConfig(headless=True, verbose=False)
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        deep_crawl_strategy=strategy,
        delay_before_return_html=2.0,
        page_timeout=30000,
        excluded_tags=["footer", "script", "style"],
        remove_overlay_elements=True,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed"),
            options={"ignore_links": False},
        ),
        stream=True,
    )

    print(f"Starting deep crawl of {BASE_URL}")
    print(f"Output: {OUTPUT_DIR}/\n")

    count = 0
    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun(BASE_URL, config=crawler_config):
            if not result.success:
                print(f"  FAIL  {result.url} — {result.error_message}")
                continue

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

            count += 1
            print(f"  [{count:>3}] {result.url} → {filename}")

    print(f"\nDone. {count} pages saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
