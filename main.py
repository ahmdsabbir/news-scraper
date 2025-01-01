from termcolor import cprint

from lib.art import ascii_art
from lib.info import info
from lib.prothom_alo import ProthomAloScraper
from lib.xml import generate_atom_feed
from lib.time import generate_published_date
from lib.directories import create_dir_if_not_exists, dir_exists

# Example usage
if __name__ == "__main__":
    ascii_art()
    info()

    print('Choices:')
    print('\t[1] for ProthomAlo: ')
    choice = input('\nChoose a number and press <Enter> ')

    if choice != '1':
        cprint('Only ProthomAlo is currently supported', 'yellow')
    else:
        pass
    
    create_dir_if_not_exists('data')
    

    if choice == '1':
        curr_date = generate_published_date()

        create_dir_if_not_exists('data/prothomalo')

        if dir_exists(f'data/prothomalo/{curr_date['readable']}.txt'):
            cprint('Looks like you already scraped ProthomAlo today.', 'red')
            cprint(f'Please delete the file: "data/prothomalo/{curr_date['readable']}.txt" before retrying', 'red')

            exit()


        scraper = ProthomAloScraper()
        scraper.fetch_and_parse()

        anchors = scraper.get_anchors()

        urls = [anchor.url for anchor in anchors]

        print(f"\n{len(urls)} news articles to be scraped.")

        atom_feed = ""
        successfull = 0

        for idx, url in enumerate(urls):
            print()
            cprint(f"{idx + 1}: Scraping url: {url}", "cyan")

            try:
                article = scraper.get_content(url)
                title = article["heading"]
                content = article["article"]

                cprint(f"\tTitle: {url}", "white")

                atom_feed = atom_feed + generate_atom_feed(title, content)

                successfull += 1
            except Exception as e:
                cprint(f"Failed to scrape url: {url}", "red")
                cprint(f"Reason: {str(e)}", "magenta")

        # Write to a text file
        with open(f"data/prothomalo/{curr_date['readable']}.txt", "w", encoding="utf-8") as file:
            file.write(atom_feed)

        cprint("Process executed. Here are the details: ", "white")
        cprint(f"Successful entries: {str(successfull)}", "cyan")
        cprint(f"    Failed entries: {str(len(urls) - successfull)}", "red")
        cprint(f"Filed saved at this location: data/prothomalo/{curr_date['readable']}.txt", 'green')