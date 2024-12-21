from xml.etree import ElementTree as ET

import os
from datetime import datetime

def get_current_date_formatted():
  """
  Gets the current date and time in the format "2-3-2014-1:05am".

  Returns:
      str: The current date and time in the specified format.
  """
  now = datetime.now()
  month = now.strftime("%m")
  day = now.strftime("%d")
  year = now.strftime("%Y")
  hour = now.strftime("%I")
  minute = now.strftime("%M")
  am_pm = now.strftime("%p")
  return f"{month}-{day}-{year}-{hour}:{minute}{am_pm.lower()}"

def generate_atom_feed(entry_id, published_date, updated_date, title, content, link, author_name, author_uri, author_email):
  """
  Generates an XML Atom feed with a single entry and writes it to a file.

  Args:
      entry_id: The unique identifier for the entry.
      published_date: The date and time the entry was published (YYYY-MM-DD format).
      updated_date: The date and time the entry was last updated (YYYY-MM-DD format with time and timezone offset).
      title: The title of the entry.
      content: The HTML content of the entry.
      link: The URL of the entry.
      author_name: The name of the author.
      author_uri: The URL of the author's profile.
      author_email: The email address of the author (can be set to 'noreply@blogger.com').
  """

  namespaces = {
      '': 'http://www.w3.org/2005/Atom',
      'openSearch': 'http://a9.com/-/spec/opensearchrss/1.0/',
      'gd': 'http://schemas.google.com/g/2005',
      'thr': 'http://purl.org/syndication/thread/1.0',
      'georss': 'http://www.georss.org/georss'
  }

  # Create the root element
  feed = ET.Element('feed', attrib=namespaces)

  # Create the entry element
  entry = ET.SubElement(feed, 'entry')

  # Add entry elements
  ET.SubElement(entry, 'id').text = entry_id
  ET.SubElement(entry, 'published').text = published_date
  ET.SubElement(entry, 'updated').text = updated_date
  category1 = ET.SubElement(entry, 'category')
  category1.attrib = {'scheme': 'http://schemas.google.com/g/2005#kind', 'term': 'http://schemas.google.com/blogger/2008/kind#post'}
  category2 = ET.SubElement(entry, 'category')
  category2.attrib = {'scheme': 'http://www.blogger.com/atom/ns#', 'term': 'Technology'}
  ET.SubElement(entry, 'title', type='text').text = title
  content_element = ET.SubElement(entry, 'content', type='html')
  content_element.text = content
  ET.SubElement(entry, 'link', rel='edit', type='application/atom+xml').attrib = {'href': link}
  ET.SubElement(entry, 'link', rel='self', type='application/atom+xml').attrib = {'href': link}
  alternate_link = ET.SubElement(entry, 'link', rel='alternate', type='text/html')
  alternate_link.attrib = {'href': link, 'title': title}

  # Create author element and sub-elements
  author = ET.SubElement(entry, 'author')
  ET.SubElement(author, 'name').text = author_name
  ET.SubElement(author, 'uri').text = author_uri
  ET.SubElement(author, 'email').text = author_email
  image = ET.SubElement(author, 'gd:image', attrib={'rel': 'http://schemas.google.com/g/2005#thumbnail', 'width': '35', 'height': '35'})
  image.attrib['src'] = '//www.blogger.com/img/blogger_logo_round_35.png'

  # Write the XML to a file
  tree = ET.ElementTree(feed)

  target_dir = 'xmls/prothomalo/'
  os.makedirs(target_dir, exist_ok=True)
  tree.write(os.path.join(target_dir, get_current_date_formatted() + '.xml'), encoding='utf-8', xml_declaration=True)

    #   tree.write(get_current_date_formatted() + '.xml', encoding='utf-8', xml_declaration=True)
    