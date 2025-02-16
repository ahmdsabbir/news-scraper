from dataclasses import dataclass
from typing import Literal



@dataclass
class PageType:
    tag: str
    attr: Literal['id', 'class']
    value: str

@dataclass
class WebsiteSettings:
    url: str
    home: PageType
    single: PageType