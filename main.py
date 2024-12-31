from lib.prothom_alo import ProthomAloScraper
from lib.xml import generate_atom_feed
from lib.time import generate_published_date
from termcolor import cprint

# Example usage
if __name__ == "__main__":
    curr_date = generate_published_date()

    scraper = ProthomAloScraper()
    scraper.fetch_and_parse()

    anchors = scraper.get_anchors()

    urls = [anchor.url for anchor in anchors]

    print(f'{len(urls)} news articles to be scraped.')

    atom_feed = ''
    successfull = 0

    for idx, url in enumerate(urls):
        print()
        cprint(f'{idx + 1}: Scraping url: {url}', "cyan")

        try:  
            article = scraper.get_content(url)
            title = article['heading']
            content = article['article']

            cprint(f'{idx + 1}: \tTitle: {url}', "light_cyan")

            atom_feed = atom_feed + generate_atom_feed(title, content)
            
            successfull += 1
        except Exception as e:
            cprint(f'Failed to scrape url: {url}', 'red')
            cprint(f'Reason: {str(e)}', 'magenta')

    # Write to a text file
    with open(f"{curr_date['readable']}.txt", "w", encoding="utf-8") as file:
        file.write(atom_feed)

    cprint("Process executed. Here are the details: ", 'white')
    cprint(f'Successful entries: {str(successfull)}', 'green')
    cprint(f'    Failed entries: {str(len(urls) - successfull)}', 'red')
