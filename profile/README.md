<div align="center">
  <img src="https://github.com/2scraper.png" width="96" alt="2scraper logo">

  <h1>2scraper</h1>

  <p><strong>Open-source web scrapers for real-world websites.</strong></p>
  <p>Turn products, listings, comments, prices, and market data into clean JSON or CSV.</p>

  <p>
    <a href="#scraper-directory"><strong>Browse scrapers</strong></a>
    ·
    <a href="https://github.com/2scraper/.github/issues/new?title=%5BScraper%20request%5D%20"><strong>Request a website</strong></a>
    ·
    <a href="#contributing"><strong>Contribute</strong></a>
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
| **🧰 Multiple execution paths**<br>Playwright, Selenium, Puppeteer, direct APIs, or remote browsers—depending on the target. | **🛡️ Built for real websites**<br>Pagination, dynamic content, proxies, fingerprints, and CAPTCHA flows where the site requires them. |

## Start in three steps

1. Pick a target from the [scraper directory](#scraper-directory).
2. Open its repository and follow the quick-start guide.
3. Run locally, then add the optional browser, proxy, or CAPTCHA setup documented for that target.

> Support differs by repository. The README in each scraper is the source of truth for engines, locales, fields, and infrastructure requirements.

## Featured scrapers

| Repository | What it extracts |
|---|---|
| [**Amazon**](https://github.com/2scraper/amazon-scraper) | Search results, best sellers, product pages, and public reviews across 21 marketplaces |
| [**YouTube**](https://github.com/2scraper/youtube-scraper) | Comment threads and replies, video metadata, and video search |
| [**Catawiki**](https://github.com/2scraper/catawiki-scraper) | Auction lots, bids, reserves, estimates, and seller data |
| [**StockX**](https://github.com/2scraper/stockx-scraper) | Products, asks, bids, last sales, and market statistics |
| [**Transfermarkt**](https://github.com/2scraper/transfermarkt-scraper) | Player profiles, market values, club squads, and transfers |
| [**Medium**](https://github.com/2scraper/medium-scraper) | Stories, authors, publications, tag feeds, and full article text |

## Scraper directory

All public platform scrapers, grouped by their primary use case.

| Category | Repositories |
|---|---|
| **E-commerce & retail** | [Amazon](https://github.com/2scraper/amazon-scraper) · [Andie Swim](https://github.com/2scraper/andieswim-scraper) · [Bershka](https://github.com/2scraper/bershka-scraper) · [Catawiki](https://github.com/2scraper/catawiki-scraper) · [Etsy](https://github.com/2scraper/etsy-scraper) · [Farfetch](https://github.com/2scraper/farfetch-scraper) · [Givenchy](https://github.com/2scraper/givenchy-scraper)<br>[Google Play](https://github.com/2scraper/googleplay-scraper) · [Home Depot](https://github.com/2scraper/homedepot-scraper) · [Maison KOSÉ](https://github.com/2scraper/kose-scraper) · [LG](https://github.com/2scraper/lg-scraper) · [Lidl](https://github.com/2scraper/lidl-scraper) · [MediaMarkt](https://github.com/2scraper/mediamarkt-scraper) · [Montblanc](https://github.com/2scraper/montblanc-scraper)<br>[OpenSea](https://github.com/2scraper/opensea-scraper) · [Rakuten](https://github.com/2scraper/rakuten-scraper) · [Sleep Number](https://github.com/2scraper/sleepnumber-scraper) · [StockX](https://github.com/2scraper/stockx-scraper) · [TikTok Shop](https://github.com/2scraper/tiktok-shop-scraper) · [Tokopedia](https://github.com/2scraper/tokopedia-scraper) · [Woolworths](https://github.com/2scraper/woolworths-scraper) |
| **Classifieds, property & travel** | [Craigslist](https://github.com/2scraper/craigslist-scraper) · [Dubizzle](https://github.com/2scraper/dubizzle-scraper) · [Flippa](https://github.com/2scraper/flippa-scraper) · [Spinny](https://github.com/2scraper/spinny-scraper) · [Vrbo](https://github.com/2scraper/vrbo-scraper) · [Zimmo](https://github.com/2scraper/zimmo-scraper) |
| **Food & delivery** | [foodpanda](https://github.com/2scraper/foodpanda-scraper) |
| **Publishing, community & video** | [BBB](https://github.com/2scraper/bbb-scraper) · [Medium](https://github.com/2scraper/medium-scraper) · [Quora](https://github.com/2scraper/quora-scraper) · [TikTok Ads](https://github.com/2scraper/tiktok-ads-scraper) · [TikTok profiles](https://github.com/2scraper/tiktok-profile-scraper) · [TikTok videos](https://github.com/2scraper/tiktok-video-scraper) · [Weibo](https://github.com/2scraper/weibo-scraper) · [YouTube](https://github.com/2scraper/youtube-scraper) |
| **Jobs & hiring** | [Just Join IT](https://github.com/2scraper/justjoin-scraper) · [Mercor](https://github.com/2scraper/mercor-scraper) · [Wellfound](https://github.com/2scraper/wellfound-scraper) |
| **Finance & fundraising** | [Google Finance](https://github.com/2scraper/google-finance-scraper) · [Indiegogo](https://github.com/2scraper/indiegogo-scraper) · [Polymarket](https://github.com/2scraper/polymarket-scraper) |
| **Sports** | [Transfermarkt](https://github.com/2scraper/transfermarkt-scraper) |

<p align="right"><a href="https://github.com/orgs/2scraper/repositories"><strong>View all repositories →</strong></a></p>

## Built to fit your workflow

Most repositories include:

- a runnable Python implementation and command-line examples;
- JSON and CSV output with documented fields;
- sample records for a quick look at the data;
- pagination and dynamic-content handling tailored to the target;
- optional integrations for [2Captcha](https://2captcha.com/), [2prx](https://2prx.com/), fingerprints, or a remote browser when needed.

Every scraper can be used on your own infrastructure. Paid services are optional unless a repository explicitly says otherwise.

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
