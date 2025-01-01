from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def get_soup(content: str) -> BeautifulSoup:
        return BeautifulSoup(content, "lxml")
