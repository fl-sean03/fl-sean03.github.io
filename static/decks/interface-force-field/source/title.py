#!/usr/bin/env python3
"""Capture the Writings title image from the deck's actual first slide at 1920 × 1080.

usage: python source/title.py index.html ../../images/writings/interface-force-field-title.png
"""
import asyncio
import os
import sys
from pathlib import Path

from playwright.async_api import async_playwright

CHROME = os.environ.get('CHROME')  # a Chromium executable to use instead of Playwright's own browser


async def main(deck, out):
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
        await page.goto(deck.as_uri() + '#1')
        await page.evaluate('window.deck.ready')
        await page.wait_for_timeout(3500)  # the start toast fades after 3 s
        assert await page.evaluate('window.deck.index') == 0 and not await page.evaluate('window.deck.reading')
        await page.locator('#deck').screenshot(path=str(out))
        await browser.close()

asyncio.run(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2])))
