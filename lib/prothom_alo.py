from lib.web_scraper import WebScraper

class ProthomAloScraper(WebScraper):
    def __init__(self):
        parser = super().__init__(url='https://www.prothomalo.com/', target_div_class='eg5Jk')