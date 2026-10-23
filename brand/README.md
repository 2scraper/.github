# 2scraper brand — logo "Prompt" (2>▮)

Chosen direction: **D · Prompt** — a shell prompt `2>` with a block cursor. Monospace (IBM Plex Mono SemiBold), text converted to paths, so nothing depends on fonts being loaded.

This folder is the single source of truth for the 2scraper logo. Use these files as they are; do not redraw the mark.

## Tokens
| token   | value     | use |
|---------|-----------|-----|
| ink     | `#F2F4F7` | the "2" and "scraper" on dark backgrounds |
| ink-on-light | `#0E1116` | the same on light backgrounds |
| accent  | `#C8F55A` | the `>` and the cursor bar — never recolor these |
| bg      | `#0E1116` | tile / avatar / OG background |

Inline variants use `currentColor` for ink, so they follow the surrounding text color automatically.

## Files
| file | what | where it goes |
|------|------|---------------|
| `logo-mark-inline.svg` | 64×64 mark, ink = currentColor, transparent | inline `<svg>` in the site header/footer |
| `logo-horizontal-inline.svg` | `2> scraper▮` wordmark, 219×48, ink = currentColor | optional: hero / footer / README banner |
| `logo-mark.svg`, `logo-mark-onlight.svg` | same mark with fixed ink, transparent | `<img>` usage, README |
| `logo-mark-tile.svg` | mark on a dark rounded tile | app icons, slide decks |
| `logo-horizontal.svg`, `logo-horizontal-onlight.svg` | wordmark with fixed ink | README banner, social |
| `favicon.svg` | `2>` only (no cursor) on dark tile — tuned for 16 px | `<link rel="icon">` |
| `favicon.ico` (16/32/48), `favicon-16.png`, `favicon-32.png`, `favicon-48.png` | raster fallbacks | site root |
| `apple-touch-icon.png` 180 | iOS home screen | site root |
| `icon-192.png`, `icon-512.png` | PWA / manifest | site root |
| `github-avatar-512.png` | full-bleed dark square, circle-safe | GitHub org avatar (Settings → Profile picture) |
| `og-image.png` 1200×630 | wordmark + tagline on dark | `og:image` / `twitter:image` |

## Clear space & minimum size
- Clear space around the mark = the width of the cursor bar (≈ 11 % of the mark height).
- Minimum: mark 20 px, wordmark 120 px wide. Below 24 px use `favicon.svg` (no cursor).

## Do not
- Change the accent on the `>` or cursor; do not add gradients, outlines or shadows.
- Set the wordmark in Syne — the lockup is deliberately all-mono; Syne stays for headings on the site.
- Put the mark on the GitHub avatar with a rounded corner — GitHub rounds it itself; `github-avatar-512.png` is already full-bleed.
