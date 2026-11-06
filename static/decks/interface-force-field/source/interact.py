#!/usr/bin/env python3
"""Check the viewer's reading and zoom controls and the slide 2 animation on a laptop and a phone, saving a screenshot
of each state.

usage: python source/interact.py index.html outdir
"""
import asyncio
import os
import sys
from pathlib import Path

from playwright.async_api import async_playwright

deck, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
CHROME = os.environ.get('CHROME')  # a Chromium executable to use instead of Playwright's own browser
results = []


def check(name, ok, detail=''):
    results.append(ok)
    print('PASS' if ok else 'FAIL', name, detail)


async def open_page(browser, w, h, hash_):
    phone = w < 700 or h < 500
    page = await browser.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2 if phone else 1,
                                  is_mobile=phone, has_touch=phone)
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    await page.goto(deck.as_uri() + hash_)
    await page.evaluate('window.deck.ready')
    await page.wait_for_timeout(400)
    return page, errors


async def state(page):
    return await page.evaluate("""() => ({reading: window.deck.reading, index: window.deck.index, hash: location.hash,
        zoom: !document.getElementById('zoom').hidden,
        pill: getComputedStyle(document.getElementById('read-pill')).opacity,
        overflow: document.documentElement.scrollWidth - innerWidth})""")


async def plays(page, selector, name, shot):
    """Check that the animation at `selector` has loaded and moves: three pictures of it 0.9 s apart differ."""
    img = page.locator(selector)
    await img.scroll_into_view_if_needed()
    loaded = await img.evaluate('im => im.complete && im.naturalWidth > 0')
    pictures = []
    for _ in range(3):
        pictures.append(await img.screenshot())
        await page.wait_for_timeout(900)
    (out / shot).write_bytes(pictures[-1])
    check(f'{name} animation loads and plays', loaded and len(set(pictures)) > 1, (loaded, len(set(pictures))))


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)

        # Laptop on slide 2: the growth animation plays beside the figure.
        page, errors = await open_page(browser, 1440, 900, '#2')
        await plays(page, 'img.animation', 'laptop slide 2', 'laptop-2-animation.png')
        await page.screenshot(path=str(out / 'laptop-2.png'))
        check('laptop slide 2 errors', not errors, errors)
        await page.close()

        # Laptop: #read opens the reading version; T and Esc go back to the slides; the pill opens it again.
        page, errors = await open_page(browser, 1440, 900, '#read')
        s = await state(page)
        check('laptop #read opens reading', s['reading'] and s['hash'] == '#read', s)
        check('laptop reading has no sideways scroll', s['overflow'] <= 0, s['overflow'])
        await page.screenshot(path=str(out / 'laptop-read-top.png'))
        await page.evaluate("document.getElementById('read-lj').scrollIntoView()")
        await page.wait_for_timeout(200)
        await page.screenshot(path=str(out / 'laptop-read-lj.png'))
        await page.keyboard.press('t')
        s = await state(page)
        check('T closes reading at the page being read', not s['reading'] and s['hash'] == '#8', s)
        await page.keyboard.press('t')
        s = await state(page)
        check('T opens reading again', s['reading'], s)
        await page.keyboard.press('Escape')
        s = await state(page)
        check('Esc closes reading', not s['reading'], s)
        await page.mouse.move(700, 450)
        await page.mouse.move(720, 460)
        await page.wait_for_timeout(300)
        s = await state(page)
        check('the pill shows on mouse movement', s['pill'] == '1', s['pill'])
        await page.click('#read-pill')
        s = await state(page)
        check('the pill opens reading', s['reading'], s)
        await page.click('#read-lj figure img')
        await page.wait_for_timeout(300)
        s = await state(page)
        check('clicking a picture enlarges it', s['zoom'], s)
        await page.screenshot(path=str(out / 'laptop-zoom-8.png'))
        await page.keyboard.press('Escape')
        s = await state(page)
        check('Esc closes the enlarged picture first', not s['zoom'] and s['reading'], s)
        await page.click('#to-slides')
        s = await state(page)
        check('the Slides button returns to the slides', not s['reading'], s)
        check('laptop errors', not errors, errors)
        await page.close()

        # Phone in portrait: the reading version opens by itself; a tap enlarges a picture.
        page, errors = await open_page(browser, 390, 844, '#1')
        s = await state(page)
        check('phone opens reading by itself', s['reading'], s)
        check('phone reading has no sideways scroll', s['overflow'] <= 0, s['overflow'])
        await page.screenshot(path=str(out / 'phone-read-top.png'))
        await plays(page, '#read-hook figure.r-anim img', 'phone reading', 'phone-read-animation.png')
        await page.screenshot(path=str(out / 'phone-read-hook.png'))
        await page.tap('#read-hook figure.r-anim img')
        await page.wait_for_timeout(300)
        s = await state(page)
        check('tapping the animation leaves it in place', not s['zoom'] and s['reading'], s)
        await page.tap('#read-agent figure img')
        await page.wait_for_timeout(300)
        s = await state(page)
        check('tapping a picture enlarges it', s['zoom'], s)
        await page.screenshot(path=str(out / 'phone-zoom-14.png'))
        await page.evaluate("document.getElementById('zoom').scrollTo(330, 0)")
        await page.wait_for_timeout(200)
        await page.screenshot(path=str(out / 'phone-zoom-14-panned.png'))
        await page.tap('#zoom .z-close')
        s = await state(page)
        check('Close shuts the enlarged picture', not s['zoom'] and s['reading'], s)
        await page.tap('#to-slides')
        await page.wait_for_timeout(300)
        s = await state(page)
        check('phone Slides button shows the slides', not s['reading'], s)
        check('and shows the way back to reading', s['pill'] == '1', s['pill'])
        await page.screenshot(path=str(out / 'phone-slides.png'))
        check('phone errors', not errors, errors)
        await page.close()

        # Phone on its side: the slides stay up for presenting.
        page, errors = await open_page(browser, 844, 390, '#5')
        s = await state(page)
        check('landscape phone keeps the slides', not s['reading'] and s['index'] == 4, s)
        check('the reading button shows at first on a touch screen', s['pill'] == '1', s['pill'])
        await page.wait_for_timeout(4500)
        s = await state(page)
        check('then it fades so the slide is clear', s['pill'] == '0', s['pill'])
        await page.screenshot(path=str(out / 'phone-landscape-5-clear.png'))
        await page.tap('#stage', position={'x': 422, 'y': 195})
        await page.wait_for_timeout(300)
        s = await state(page)
        check('a touch brings it back', s['pill'] == '1', s['pill'])
        await page.screenshot(path=str(out / 'phone-landscape-5.png'))
        check('landscape errors', not errors, errors)
        await page.close()

        # A reader who asks for reduced motion sees the still instead.
        page = await browser.new_page(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
        await page.goto(deck.as_uri() + '#2')
        await page.evaluate('window.deck.ready')
        shown = await page.evaluate("[...document.querySelectorAll('picture img')].map(im => im.currentSrc)")
        check('reduced motion shows the still', len(shown) == 2 and all(s.endswith('.jpg') for s in shown), shown)
        await browser.close()
    print(sum(results), 'of', len(results), 'checks passed')

asyncio.run(main())
sys.exit(not all(results))
