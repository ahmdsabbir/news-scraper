from termcolor import cprint

def ascii_art():
  """Prints the given ASCII art."""

  art = """
 ___  ___ _ __ __ _ _ __   ___ _ __ 
/ __|/ __| '__/ _` | '_ \ / _ \ '__|
\__ \ (__| | | (_| | |_) |  __/ |   
|___/\___|_|  \__,_| .__/ \___|_|   
                   | |              
                   |_|                     
                                                                                               88                                 
"""
  cprint(art, 'blue')

if __name__ == '__main__':
  ascii_art()
