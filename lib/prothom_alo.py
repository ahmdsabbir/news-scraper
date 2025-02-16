from lib.web_scraper import WebScraper
from src.typesafety.settings import WebsiteSettings, PageType

class ProthomAloScraper(WebScraper):
    def __init__(self):
        parser = super().__init__(
            siteConfig=WebsiteSettings(
                url='https://www.prothomalo.com/',
                home=PageType(
                    tag='div',
                    attr='class',
                    value='eg5Jk'
                ),
                single=PageType(
                    tag='div',
                    attr='class',
                    value='container'
                )
            )
        )
