from termcolor import cprint
from config import config

def info():
  cprint(f'Desc        :   {config["desc"]}', 'blue', attrs=["reverse", "blink"])
  cprint(f'Version     :   {config["version"]}', 'blue')
  cprint(f'Github Repo :   {config["git-repo"]}', 'blue')
  cprint(f'Author      :   {config["author"]}', 'blue')
  cprint(f'Author URI  :   {config["author-uri"]}', 'blue')
  cprint(f'Author email:   {config["author-email"]}', 'blue')

if __name__ == '__main__':
  info()