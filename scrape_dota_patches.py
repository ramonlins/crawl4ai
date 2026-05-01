"""
Scrape all Dota 2 patches from https://www.dota2.com/patches/
Discovers all version numbers from the page, then crawls each one.
Output: dota_patches/ with one markdown file per patch.
"""

import asyncio
import os
import re
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

OUTPUT_DIR = "dota_patches"
BASE_URL = "https://www.dota2.com/patches/"


def version_sort_key(v: str):
    """Sort patch versions numerically, e.g. 7.39b > 7.39a > 7.39."""
    parts = v.split(".")
    minor = parts[1] if len(parts) > 1 else "0"
    num = int(re.sub(r"[a-z]+$", "", minor))
    suffix = re.search(r"[a-z]+$", minor)
    return (int(parts[0]), num, suffix.group() if suffix else "")


async def get_all_versions(crawler) -> list[str]:
    """Scrape the index page and extract all patch version strings."""
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        delay_before_return_html=4.0,
        page_timeout=30000,
    )
    result = await crawler.arun(BASE_URL, config=config)
    html = result.html or ""
    versions = re.findall(r'\b7\.\d+[a-z]?\b', html)
    unique = sorted(set(versions), key=version_sort_key, reverse=True)
    return unique


async def scrape_patch(crawler, version: str, config: CrawlerRunConfig) -> str | None:
    url = f"{BASE_URL}{version}"
    result = await crawler.arun(url, config=config)
    if not result.success:
        return None
    content = (
        result.markdown.fit_markdown
        if result.markdown and result.markdown.fit_markdown
        else result.markdown.raw_markdown if result.markdown else ""
    )
    return content


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    browser_config = BrowserConfig(headless=True, verbose=False)

    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,
        delay_before_return_html=3.0,
        page_timeout=30000,
        excluded_tags=["nav", "footer", "script", "style"],
        remove_overlay_elements=True,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.3, threshold_type="fixed"),
            options={"ignore_links": True},
        ),
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        print("Discovering patch versions...")
        versions = await get_all_versions(crawler)
        print(f"Found {len(versions)} patches: {versions[0]} → {versions[-1]}\n")

        for i, version in enumerate(versions, 1):
            filepath = os.path.join(OUTPUT_DIR, f"patch_{version}.md")
            if os.path.exists(filepath):
                print(f"  [{i:>3}/{len(versions)}] {version} — already exists, skipping")
                continue

            content = await scrape_patch(crawler, version, crawl_config)
            if content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# Dota 2 Patch {version}\n")
                    f.write(f"# Source: {BASE_URL}{version}\n\n")
                    f.write(content)
                print(f"  [{i:>3}/{len(versions)}] {version} → patch_{version}.md")
            else:
                print(f"  [{i:>3}/{len(versions)}] {version} — FAILED")

    saved = len(os.listdir(OUTPUT_DIR))
    print(f"\nDone. {saved} patches saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
