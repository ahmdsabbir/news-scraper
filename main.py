from lib.prothom_alo import ProthomAloScraper


if __name__ == "__main__":
    scraper = ProthomAloScraper()
    scraper.fetch_and_parse()

    anchors = scraper.get_anchors()

    for a in anchors:
        print(a.text)
        print(a.url)
        print("--------------------------")
