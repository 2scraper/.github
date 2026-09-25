<div align="center">
  <img src="https://github.com/2scraper.png" width="96" alt="2scraper logo">

  <h1>2scraper</h1>

  <p><strong>Open-source web scrapers for real-world websites.</strong></p>
  <p>Turn products, listings, comments, prices, and market data into clean JSON or CSV.</p>

  <p>
    <a href="#user-content-scraper-directory"><strong>Browse scrapers</strong></a>
    ·
    <a href="https://github.com/2scraper/.github/issues/new?title=%5BScraper%20request%5D%20"><strong>Request a website</strong></a>
    ·
    <a href="#user-content-contributing"><strong>Contribute</strong></a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/scrapers-30%2B-0969da?style=flat-square" alt="30+ scrapers">
    <img src="https://img.shields.io/badge/Python-powered-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python powered">
    <img src="https://img.shields.io/badge/output-JSON%20%7C%20CSV-1f883d?style=flat-square" alt="JSON and CSV output">
    <img src="https://img.shields.io/badge/open-source-f6f8fa?style=flat-square" alt="Open source">
  </p>
</div>

---

## Web data, without rebuilding the plumbing

**2scraper** is a collection of focused, ready-to-run scrapers for popular websites. Each repository targets one platform and documents the supported pages, captured fields, setup, and output—so you can spend less time reverse-engineering websites and more time using the data.

| | |
|---|---|
| **⚡ Ready to run**<br>Clone a repository, follow its quick start, and collect data on your own infrastructure. | **📦 Structured by default**<br>Predictable records in JSON or CSV, with schemas and sample output where available. |
| **🧰 Multiple execution paths**<br>Playwright, Selenium, Puppeteer, the site's own JSON endpoints, or the [2Captcha Scraping Browser API](https://2captcha.com/scraper/browser-api)—depending on the target. | **🛡️ Built for real websites**<br>Pagination, dynamic content, proxies, fingerprints, and CAPTCHA flows where the site requires them. |

## Start in three steps

1. Pick a target from the [scraper directory](#user-content-scraper-directory).
2. Open its repository and follow the quick-start guide.
3. Run locally, then add the optional browser, proxy, or CAPTCHA setup documented for that target.

> Support differs by repository. The README in each scraper is the source of truth for engines, locales, fields, and infrastructure requirements.

## Featured scrapers

| Repository | What it extracts |
|---|---|
| [**Amazon**](https://github.com/2scraper/amazon-scraper) | Search results, best sellers, product pages, and public reviews across 21 marketplaces — runs with no key or proxy |
| [**YouTube**](https://github.com/2scraper/youtube-scraper) | Comment threads and replies, video metadata, and video search — runs with no key or proxy |
| [**Catawiki**](https://github.com/2scraper/catawiki-scraper) | Auction lots, bids, reserves, estimates, and seller data — runs with no key or proxy |
| [**StockX**](https://github.com/2scraper/stockx-scraper) | Products, asks, bids, last sales, and market statistics |
| [**Transfermarkt**](https://github.com/2scraper/transfermarkt-scraper) | Player profiles, market values, club squads, and transfers |
| [**Medium**](https://github.com/2scraper/medium-scraper) | Stories, authors, publications, tag feeds, and full article text — runs with no key or proxy |

## Scraper directory

All public platform scrapers, grouped by what they are used for.

🟢 runs with **no API key and no proxy** · 🔵 needs the **[2Captcha Scraping Browser API](https://2captcha.com/scraper/browser-api)** — both measured and dated in that repository's README.

> **One platform can take more than one scraper.** TikTok gates each route differently, so it is covered by four that work side by side: [profiles](https://github.com/2scraper/tiktok-profile-scraper) 🟢, [videos](https://github.com/2scraper/tiktok-video-scraper) 🟢 and the [EU Ad Library](https://github.com/2scraper/tiktok-ads-scraper) 🟢 need no key at all; [TikTok Shop](https://github.com/2scraper/tiktok-shop-scraper) 🔵 is behind a captcha and needs the Scraping Browser.

### 🛒 E-commerce & retail

| Scraper | What it extracts |
|---|---|
| [**Amazon**](https://github.com/2scraper/amazon-scraper) 🟢 | Search results, best sellers, product pages and reviews |
| [**Andie Swim**](https://github.com/2scraper/andieswim-scraper) 🟢 | Swimwear listings, per-size stock and prices |
| [**Bershka**](https://github.com/2scraper/bershka-scraper) | Inditex catalogue, one row per SKU |
| [**Catawiki**](https://github.com/2scraper/catawiki-scraper) 🟢 | Auction lots, bids, reserves, estimates, sellers |
| [**Etsy**](https://github.com/2scraper/etsy-scraper) 🔵 | Search, category, shop and listing pages |
| [**Farfetch**](https://github.com/2scraper/farfetch-scraper) | Fashion listings and product pages with prices |
| [**Givenchy**](https://github.com/2scraper/givenchy-scraper) 🟢 | Beauty products and prices |
| [**Home Depot**](https://github.com/2scraper/homedepot-scraper) | Category listings and product pages, prices, specs |
| [**Maison KOSÉ**](https://github.com/2scraper/kose-scraper) 🟢 | Japanese cosmetics: products, prices, brands, stock |
| [**LG**](https://github.com/2scraper/lg-scraper) 🟢 | Catalogue models, sizes and categories |
| [**Lidl**](https://github.com/2scraper/lidl-scraper) | US grocery products, prices, unit prices |
| [**MediaMarkt**](https://github.com/2scraper/mediamarkt-scraper) | Electronics listings and product pages, prices |
| [**Montblanc**](https://github.com/2scraper/montblanc-scraper) 🟢 | Per-market prices, stock, collections, variants |
| [**Rakuten**](https://github.com/2scraper/rakuten-scraper) 🟢 | Ichiba products, prices, points, shops, reviews |
| [**Sleep Number**](https://github.com/2scraper/sleepnumber-scraper) | Smart beds and mattresses: per-size prices, ratings |
| [**StockX**](https://github.com/2scraper/stockx-scraper) | Sneaker listings and products: asks, bids, last sale |
| [**TikTok Shop**](https://github.com/2scraper/tiktok-shop-scraper) 🔵 | Products, prices, units sold, sellers |
| [**Tokopedia**](https://github.com/2scraper/tokopedia-scraper) 🔵 | Indonesian marketplace: search, category, product pages |
| [**Woolworths**](https://github.com/2scraper/woolworths-scraper) 🟢 | Supermarket products, prices, unit prices, specials |

### 🏠 Classifieds, property & travel

| Scraper | What it extracts |
|---|---|
| [**Autotrader**](https://github.com/2scraper/autotrader-scraper) | US car listings and detail pages: price, KBB fair price, VIN, dealers |
| [**Craigslist**](https://github.com/2scraper/craigslist-scraper) 🟢 | Classified listings and postings |
| [**dubizzle**](https://github.com/2scraper/dubizzle-scraper) | UAE classifieds: cars, property, jobs |
| [**Flippa**](https://github.com/2scraper/flippa-scraper) 🟢 | Online businesses, websites, apps and domains for sale |
| [**MakeMyTrip**](https://github.com/2scraper/makemytrip-scraper) 🔵 | Indian hotel listings: nightly prices with taxes and fees, star and guest ratings |
| [**Spinny**](https://github.com/2scraper/spinny-scraper) 🟢 | Used-car listings and car pages, prices |
| [**Vrbo**](https://github.com/2scraper/vrbo-scraper) | Vacation-rental search grids and property pages |
| [**Zimmo**](https://github.com/2scraper/zimmo-scraper) | Belgian property listings: prices, area, bedrooms, EPC |

### 🍔 Food & delivery

| Scraper | What it extracts |
|---|---|
| [**foodpanda**](https://github.com/2scraper/foodpanda-scraper) | Restaurant listings, ratings, cuisines, deals |

### 📱 Apps, social & video

| Scraper | What it extracts |
|---|---|
| [**Google Play**](https://github.com/2scraper/googleplay-scraper) 🟢 | App listings, search, installs, ratings and reviews |
| [**Snapchat**](https://github.com/2scraper/snapchat-scraper) 🟢 | Public profiles, subscriber counts, Spotlight views and engagement, stories and highlights |
| [**TikTok Ad Library**](https://github.com/2scraper/tiktok-ads-scraper) 🟢 | EU ads: advertisers, creatives, run dates, audience bucket |
| [**TikTok profiles**](https://github.com/2scraper/tiktok-profile-scraper) 🟢 | Exact follower, like and video counts, bio |
| [**TikTok videos**](https://github.com/2scraper/tiktok-video-scraper) 🟢 | Captions, engagement, hashtags, subtitles, media URLs |
| [**Weibo**](https://github.com/2scraper/weibo-scraper) 🟢 | Hot feed, account timelines, comments, engagement |
| [**YouTube**](https://github.com/2scraper/youtube-scraper) 🟢 | Comment threads and replies, video metadata, search |

### 📝 Publishing & Q&A

| Scraper | What it extracts |
|---|---|
| [**Medium**](https://github.com/2scraper/medium-scraper) 🟢 | Tag feeds, archives, author pages, full story text |
| [**Quora**](https://github.com/2scraper/quora-scraper) 🟢 | Answers from questions, profiles and topics |

### 💼 Jobs & business directories

| Scraper | What it extracts |
|---|---|
| [**BBB**](https://github.com/2scraper/bbb-scraper) | Business listings, BBB ratings, accreditation, complaints |
| [**Just Join IT**](https://github.com/2scraper/justjoin-scraper) 🟢 | IT job offers with salaries, skills, seniority |
| [**Mercor**](https://github.com/2scraper/mercor-scraper) 🟢 | Contract roles, rates, eligibility, corporate openings |
| [**Wellfound**](https://github.com/2scraper/wellfound-scraper) | Startup jobs with salary and equity ranges |

### 📈 Finance, markets & fundraising

| Scraper | What it extracts |
|---|---|
| [**Binance**](https://github.com/2scraper/binance-scraper) 🟢 | P2P adverts, copy-trading lead portfolios, announcements |
| [**Google Finance**](https://github.com/2scraper/google-finance-scraper) 🟢 | Quotes, financials, analyst ratings, OHLCV, FX |
| [**Indiegogo**](https://github.com/2scraper/indiegogo-scraper) 🟢 | Campaigns, funding totals, backers, reward tiers |
| [**OpenSea**](https://github.com/2scraper/opensea-scraper) 🟢 | NFT floor prices, offers, sales history, rankings |
| [**Polymarket**](https://github.com/2scraper/polymarket-scraper) 🟢 | Prediction-market prices, order books, token ids |

### ⚽ Sports

| Scraper | What it extracts |
|---|---|
| [**Transfermarkt**](https://github.com/2scraper/transfermarkt-scraper) | Market values, squads, transfers, player profiles |

<p align="right"><a href="https://github.com/orgs/2scraper/repositories"><strong>View all repositories →</strong></a></p>

## Built to fit your workflow

Most repositories include:

- a runnable Python implementation and command-line examples;
- JSON and CSV output with documented fields;
- sample records for a quick look at the data;
- pagination and dynamic-content handling tailored to the target;
- optional [2Captcha](https://2captcha.com/) integrations — [captcha solving](https://2captcha.com/), the [Scraping Browser API](https://2captcha.com/scraper/browser-api), [2prx](https://2prx.com/) residential proxies and [fingerprints](https://2captcha.com/s/fingerprints) — when a site needs them.

Every scraper can be used on your own infrastructure. Paid services are optional unless a repository explicitly says otherwise.

## 2Captcha products, one account

Every scraper runs on your own machine first. When a site pushes back, each repository says which of these helps — and which does not — with the measurement behind it.

| Product | What it gives a scraper | Where it matters here |
|---|---|---|
| [**Scraping Browser API**](https://2captcha.com/scraper/browser-api) | A managed Chrome over CDP with its own exit country, persistent profiles and captcha auto-solve — no browser or residential address of your own | The 🔵 scrapers, and any server-side pipeline that cannot run a headful browser from a home address |
| [**Captcha solving**](https://2captcha.com/) | Tokens for reCAPTCHA, Cloudflare Turnstile and other challenge widgets | Sites that put a challenge widget in front of their pages |
| [**Residential proxies**](https://2prx.com/) | Residential exits by country | Sites that refuse datacentre addresses — the repositories without 🟢 say so |
| [**Fingerprints**](https://2captcha.com/s/fingerprints) | A consistent, self-consistent browser identity | Volume across many sessions |

The four are billed separately; one [2Captcha account](https://2captcha.com/) covers them.

## Need another website?

If the target is not listed, [open a scraper request](https://github.com/2scraper/.github/issues/new?title=%5BScraper%20request%5D%20) with the website, pages you need, desired fields, and expected scale. For a private or custom extraction project, [start an inquiry](https://github.com/2scraper/.github/issues/new?title=%5BInquiry%5D%20).

## Contributing

- **Found a bug?** Open an issue in the affected scraper repository and include the URL, command, and relevant log output.
- **Want to improve a scraper?** Fork the repository and send a focused pull request.
- **Missing a platform?** [Request it here](https://github.com/2scraper/.github/issues/new?title=%5BScraper%20request%5D%20).

Please use scraped data responsibly and follow the target website's terms and applicable laws.

---

<p align="center">
  Built for developers and data teams who would rather use the data than fight the page.
</p>
