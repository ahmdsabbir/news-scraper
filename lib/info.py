from termcolor import cprint

def info():
  cprint('Desc        :   Scraper News from papers and save in blogger.com importable XML', 'blue', attrs=["reverse", "blink"])
  cprint('Version     :   1.0.0', 'blue')
  cprint('Github Repo :   github@ahmdsabbir/news-scraper', 'blue')
  cprint('Author      :   Sabbir Ahmed', 'blue')
  cprint('Author URI  :   github@ahmdsabbir', 'blue')

if __name__ == '__main__':
  info()