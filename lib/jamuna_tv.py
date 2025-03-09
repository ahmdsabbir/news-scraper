from lib.web_scraper import WebScraper
from src.typesafety.settings import WebsiteSettings, PageType
from dataclasses import dataclass
from typing import List
from bs4 import BeautifulSoup, Tag

@dataclass
class Anchor:
    text: str
    url: str

class JamunaTvScraper(WebScraper):
    def __init__(self):
        parser = super().__init__(
            siteConfig=WebsiteSettings(
                url='https://jamuna.tv/',
                home=PageType(
                    tag='main',
                    attr='class',
                    value='container'
                ),
                single=PageType(
                    tag='div',
                    attr='class',
                    value='article-content'
                )
            )
        )

    def get_anchors(self) -> List[Anchor]:
        print('reached Child Class')
        if not self.soup:
            raise Exception(
                "Soup not initialized. Please call fetch_and_parse() first."
            )

        # main_div = self.soup.find("div", class_=self.target_div_class)
        print('config: ', self.siteConfig)
        match self.siteConfig.home.attr:
            case 'class':
                main_div = self.soup.find(
                    self.siteConfig.home.tag,
                    class_=self.siteConfig.home.value
                )
            case 'id':
                main_div = self.soup.find(
                    self.siteConfig.home.tag,
                    id=self.siteConfig.home.value
                )

        if not main_div:
            raise Exception(f"No div with class {self.siteConfig.home.value} found")
        
        if not isinstance(main_div, Tag):
            raise Exception(f"No valid div with class {self.siteConfig.home.value} found")

        h3s = main_div.find_all("h5")
        if not h3s:
            raise Exception("No h3 tags found")

        anchors: List[Anchor] = []
        for h3 in h3s:
            a_tag = h3.find("a")
            if a_tag:
                href = a_tag.get("href")
                text = a_tag.get_text(strip=True)
                if href and text:
                    anchors.append(Anchor(text=text, url=href))

        print('anchor Len: ', len(anchors))
        print('anchors: ', anchors)

        return anchors
