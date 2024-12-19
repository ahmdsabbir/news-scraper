# app config
from new.interfaces.config_interface import Config, SiteConfig

config: list[Config] = [
  Config(
    site_name='Prothom Alo',
    url='https://prothomalo.com',
    selectors=SiteConfig(
      element='div',
      element_attr='class',
      attr_val='eg5Jk'
    )
  )
]