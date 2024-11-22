from lib.prothom_alo import ProthomAloScraper


if __name__ == "__main__":
    scraper = ProthomAloScraper()
    scraper.fetch_and_parse()

    anchors = scraper.get_anchors()

    urls = [anchor.url for anchor in anchors]


    for idx, url in enumerate(urls):
        if idx == 1:
            break

        article = scraper.get_content(url)

        print(article)