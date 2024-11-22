from typing import Optional, List
from lib.request_handler import RequestHandler
from bs4 import BeautifulSoup
from lib.parser import Parser
from dataclasses import dataclass


@dataclass
class Anchor:
    text: str
    url: str


class WebScraper:
    def __init__(self, url: str, target_div_class: str):
        self.url = url
        self.target_div_class = target_div_class
        self.soup: Optional[BeautifulSoup] = None

    def fetch_and_parse(self):
        response = RequestHandler.make_request(self.url)
        content = response.content
        self.soup = Parser.get_soup(content)

    def get_anchors(self) -> List[Anchor]:
        if not self.soup:
            raise Exception(
                "Soup not initialized. Please call fetch_and_parse() first."
            )

        main_div = self.soup.find("div", class_=self.target_div_class)
        if not main_div:
            raise Exception(f"No div with class {self.target_div_class} found")

        h3s = main_div.find_all("h3")
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

        return anchors
    

    # def get_content(self, url: str):
    #     print('url: ', url)
    #     response = RequestHandler.make_request(url)
    #     content = response.content
    #     soup = Parser.get_soup(content)

    #     # main_div = soup.find('div', class_='VzzDZ')        

    #     # ps = main_div.find_all('p')

    #     ps = soup.find_all('p')

    #     if not ps:
    #         raise Exception("No p tags found")
        
    #     article: str = ''

    #     for p in ps:
    #         p_content = p.get_text(strip=True)

    #         if (p_content is not None and len(p_content) > 50):
    #             article = article + '<p>' + p_content + "</p>"

        
    #     return content

    def get_content(self, url: str) -> str:
        response = RequestHandler.make_request(url)
        content = response.content
        soup = Parser.get_soup(content)
        
        # Find the main container div (assuming it has a specific class or id)
        main_container = soup.find('div', class_='container')  # Replace 'your-container-class' with the actual class of your container div
        
        if not main_container:
            raise Exception("No container div found")
        
        article: str = ''
        # Iterate over each child div within the main container
        for child_div in main_container.find_all('div', recursive=False):
            # For each child div, find all <p> tags
            ps = child_div.find_all('p')
            for p in ps:
                p_content = p.get_text(strip=True)
                if p_content and len(p_content) > 50:
                    article += f'<p>{p_content}</p>'
        
        return article