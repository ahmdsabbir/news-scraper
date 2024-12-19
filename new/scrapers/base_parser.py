from bs4 import BeautifulSoup

from new.interfaces.config_interface import Config

class BaseParser():
    def __init__(self, content: str, site_config: Config):
        self.config: Config = site_config

        if content is None:
            raise Exception('Content is empty')
        
        self.soup = BeautifulSoup(content)

        if self.soup is None:
            raise Exception('Something went wrong')

    def getSoup(self):
        return self.soup    

    