from lib.prothom_alo import ProthomAloScraper
from lib.xml import generate_atom_feed, Entry

from datetime import datetime, timedelta, timezone

def generate_published_date():
  """Generates a published_date string in the format "YYYY-MM-DDTHH:MM:SS.000-08:00"."""

  # Get current UTC time
  utc_now = datetime.now(timezone.utc)

  # Calculate PST time (UTC-8)
  pst_now = utc_now - timedelta(hours=8)

  # Format the PST time as the desired string
  published_date = pst_now.strftime("%Y-%m-%dT%H:%M:%S.%f%z") 

  return published_date

if __name__ == "__main__":
    scraper = ProthomAloScraper()
    scraper.fetch_and_parse()

    anchors = scraper.get_anchors()

    urls = [anchor.url for anchor in anchors]

    entries: list[Entry] = []

    for idx, url in enumerate(urls):
        article = scraper.get_content(url)
        entries.append(
           Entry(
              entry_id="tag:blogger.com,1999:blog-5968071689632345895.post-207570408380315315",
              published_date=generate_published_date(),
              update_date=generate_published_date(),
              title=article['heading'],
              content=article["article"],
              link="https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315",
              author_name="Khobor Dunia",
              author_email="noreply@blogger.com",
              author_uri="https://www.blogger.com/profile/06693327077864093576",
           )
        )
        # entry_id = "tag:blogger.com,1999:blog-5968071689632345895.post-207570408380315315"
        # published_date = generate_published_date()
        # updated_date = generate_published_date()
        # title = article['heading']
        # content = article['article']
        # link = "https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315"
        # author_name = "Khobor Dunia"
        # author_uri = "https://www.blogger.com/profile/06693327077864093576"
        # author_email = "noreply@blogger.com"

    
    generate_atom_feed(entries=entries)
