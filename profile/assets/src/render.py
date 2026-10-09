"""Render the two designs to PNG at 2x (banner) and 1x 500px (logo)."""
from playwright.sync_api import sync_playwright

import os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, w, h, scale in (("banner", 1280, 320, 2), ("logo", 500, 500, 1)):
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
        pg.goto("file://" + D + name + ".html", wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(500)
        fams = pg.evaluate("[...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight)")
        pg.screenshot(path=D + "../" + name + ".png", clip={"x": 0, "y": 0, "width": w, "height": h})
        print(name, "fonts loaded:", sorted(set(fams)))
    b.close()
