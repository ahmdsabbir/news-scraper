from dataclasses import dataclass

from typing import Literal

@dataclass
class SiteConfig:
  element: Literal['div', 'main', 'section', 'article']
  element_attr: Literal['class', 'id']
  attr_val: str

@dataclass
class Config:
  site_name: str
  url: str
  homepage: SiteConfig
  single_page: SiteConfig