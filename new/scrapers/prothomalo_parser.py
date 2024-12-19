from dataclasses import dataclass
from bs4 import BeautifulSoup

from new.scrapers.base_parser import BaseParser

from new.interfaces.parser_interface import MainDiv
from new.interfaces.config_interface import Config

@dataclass
class Anchor:
    text: str
    url: str

class ProthomAloParser():
  def __init__(self, config: Config):
    self.config: Config = config
    
    self.siteConfig = self.config['prothomalo']

    if self.siteConfig is None:
      raise Exception('Config for "prothomalo" not found')


  def get_home_anchors(self, content: str):
    soup = BaseParser(content).getSoup()

    main_div = self._get_main_div(soup)

    anchors = self._parse_anchors(main_div)

    if (len(anchors) == 0):
      raise Exception('No Anchor found for for given config in ProthomAlo')
    
    return anchors

  def _get_main_div(self, soup: BeautifulSoup):

    main_div: MainDiv = None

    if (self.config.homepage.element_attr == 'class'):
      main_div = soup.find(
        name=self.config.homepage.element,
        class_=self.config.homepage.attr_val
      )
    elif (self.config.homepage.element_attr == 'id'):
      main_div = soup.find(
        name=self.config.homepage.element,
        id=self.config.homepage.attr_val
      )
    
    if main_div is None:
      raise Exception('Main Div not found for config: ' + self.config.__str__)
    
    return main_div

  def _parse_anchors(self, main_div: BeautifulSoup) -> list[Anchor]:
    if not main_div:
      raise Exception(
          "Soup not initialized. Please call fetch_and_parse() first."
      )

    h3s = main_div.find_all("h3")

    if not h3s:
        raise Exception("No h3 tags found")

    anchors: list[Anchor] = []

    for h3 in h3s:
        a_tag = h3.find("a")
        if a_tag:
            href = a_tag.get("href")
            text = a_tag.get_text(strip=True)
            if href and text:
                anchors.append(Anchor(text=text, url=href))

    return anchors

  def get_singlepage_content(self, content: str):
    soup = BaseParser(content).getSoup()

    if (self.config.single_page.element_attr == 'class'):
      main_container = soup.find(
          name=self.config.single_page.element,
          class_=self.config.single_page.attr_val
      )
    elif (self.config.single_page.element_attr == 'id'):
       main_container = soup.find(
          name=self.config.single_page.element,
          id=self.config.single_page.attr_val
       )

    if main_container is None:
      raise Exception("No container div found")
    
    article: str = ''

    # Iterate over each child element within the main container
    for child_div in main_container.find_all('div', recursive=False):
        # For each child element, find all <p> tags
        ps = child_div.find_all('p')
        for p in ps:
            p_content = p.get_text(strip=True)
            if p_content and len(p_content) > 50:
                article += f'<p>{p_content}</p>'
    
    return article