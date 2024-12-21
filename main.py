from lib.prothom_alo import ProthomAloScraper
from lib.xml import generate_atom_feed

if __name__ == "__main__":
    scraper = ProthomAloScraper()
    scraper.fetch_and_parse()

    anchors = scraper.get_anchors()

    urls = [anchor.url for anchor in anchors]


    for idx, url in enumerate(urls):
        article = scraper.get_content(url)

        entry_id = "tag:blogger.com,1999:blog-5968071689632345895.post-207570408380315315"
        published_date = "2024-12-18T06:29:00.000-08:00"
        updated_date = "2024-12-18T06:29:46.120-08:00"
        title = article['heading']
        content = article['article']
        link = "https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315"
        author_name = "Khobor Dunia"
        author_uri = "https://www.blogger.com/profile/06693327077864093576"
        author_email = "noreply@blogger.com"

        generate_atom_feed(entry_id, published_date, updated_date, title, content, link, author_name, author_uri, author_email)