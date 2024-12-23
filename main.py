# from lib.prothom_alo import ProthomAloScraper
# from lib.xml import generate_atom_feed

# from datetime import datetime, timedelta, timezone

# def generate_published_date():
#   """Generates a published_date string in the format "YYYY-MM-DDTHH:MM:SS.000-08:00"."""

#   # Get current UTC time
#   utc_now = datetime.now(timezone.utc)

#   # Calculate PST time (UTC-8)
#   pst_now = utc_now - timedelta(hours=8)

#   # Format the PST time as the desired string
#   published_date = pst_now.strftime("%Y-%m-%dT%H:%M:%S.%f%z") 

#   return published_date

# if __name__ == "__main__":
#     scraper = ProthomAloScraper()
#     scraper.fetch_and_parse()

#     anchors = scraper.get_anchors()

#     urls = [anchor.url for anchor in anchors]


#     for idx, url in enumerate(urls):
#         article = scraper.get_content(url)

#         entry_id = "tag:blogger.com,1999:blog-5968071689632345895.post-207570408380315315"
#         published_date = generate_published_date()
#         updated_date = generate_published_date()
#         title = article['heading']
#         content = article['article']
#         link = "https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315"
#         author_name = "Khobor Dunia"
#         author_uri = "https://www.blogger.com/profile/06693327077864093576"
#         author_email = "noreply@blogger.com"

#         generate_atom_feed(entry_id, published_date, updated_date, title, content, link, author_name, author_uri, author_email)

from lib.prothom_alo import ProthomAloScraper
from lib.xml import generate_atom_feed
from datetime import datetime, timedelta, timezone
import os
from xml.etree import ElementTree as ET

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

    # Create the root element for the feed
    namespaces = {
        '': 'http://www.w3.org/2005/Atom',
        'openSearch': 'http://a9.com/-/spec/opensearchrss/1.0/',
        'gd': 'http://schemas.google.com/g/2005',
        'thr': 'http://purl.org/syndication/thread/1.0',
        'georss': 'http://www.georss.org/georss'
    }
    feed = ET.Element('feed', attrib=namespaces)

    # Iterate over each article and generate the corresponding Atom entry
    for idx, url in enumerate(urls):
        article = scraper.get_content(url)

        entry_id = "tag:blogger.com,1999:blog-5968071689632345895.post-207570408380315315"
        published_date = generate_published_date()
        updated_date = generate_published_date()
        title = article['heading']
        content = article['article']
        link = "https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315"
        author_name = "Khobor Dunia"
        author_uri = "https://www.blogger.com/profile/06693327077864093576"
        author_email = "noreply@blogger.com"

        # Generate the atom entry and append it to the feed
        entry = generate_atom_feed(entry_id, published_date, updated_date, title, content, link, author_name, author_uri, author_email)
        feed.append(entry)

    # Write the XML tree to a single file
    target_dir = 'xmls/prothomalo/'
    os.makedirs(target_dir, exist_ok=True)

    # Create the complete Atom feed and write it to a single XML file
    tree = ET.ElementTree(feed)
    tree.write(os.path.join(target_dir, 'atom_feed.xml'), encoding='utf-8', xml_declaration=True)
