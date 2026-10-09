# Profile images

`banner.png` (2560×640, shown at 1280×320) and `logo.png` (500×500, the org avatar)
are rendered from the HTML beside this file:

```bash
pip install playwright && playwright install chromium
python3 render.py        # writes ../banner.png and ../logo.png
```

The banner states counts — total scrapers, how many run with no key and no proxy (🟢),
how many need the Scraping Browser API (🔵) — taken from the directory in
`../../README.md` on 2026-10-09 (65 / 31 / 7). They go stale as repos are added:
recount from the directory, edit `banner.html` (the headline, the legend and the tile
list), re-render, and update the `alt` text in the README to match.
