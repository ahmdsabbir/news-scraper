from xml.etree import ElementTree
from datetime import datetime

def create_blog_post_xml(title, content, labels=[]):
    """
    Creates an XML element representing a new blog post.

    Args:
        title: The title of the blog post.
        content: The content of the blog post (HTML format).
        labels: A list of labels for the post.

    Returns:
        The root element of the new blog post XML element.
    """

    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    post = ElementTree.Element("entry", xmlns="http://www.w3.org/2005/Atom")
    title_elem = ElementTree.SubElement(post, "title")
    title_elem.text = title
    updated_elem = ElementTree.SubElement(post, "updated")
    updated_elem.text = now
    content_elem = ElementTree.SubElement(post, "content", type="html")
    content_elem.text = content

    for label in labels:
        category_elem = ElementTree.SubElement(post, "category", scheme="http://www.blogger.com/atom/ns#")
        category_elem.text = label

    return post

# Example usage
new_post = create_blog_post_xml(
    title="My New Blog Post",
    content="<p>This is the content of my new blog post.</p>",
    labels=["python", "programming"]
)

def append_post_to_feed(feed_file, post_element):
    """
    Appends a new post element to an existing Blogger XML feed.

    Args:
        feed_file: The path to the existing Blogger XML feed file.
        post_element: The root element of the new post XML element.
    """

    tree = ElementTree.parse(feed_file)
    root = tree.getroot()
    root.append(post_element)

    tree.write(feed_file, encoding="utf-8", xml_declaration=True)

# Example usage
# Assuming you have a Blogger XML feed named 'my_blog_feed.xml'
append_post_to_feed("base.xml", new_post)


def generate_atom_feed(title, subtitle, link, entries):
  """Generates an Atom feed using ElementTree.

  Args:
    title: The title of the feed.
    subtitle: The subtitle of the feed.
    link: The link to the feed.
    entries: A list of dictionaries, each containing 'title', 'link', 'published', and 'summary' keys.
  """

  feed = ElementTree.Element('feed')
  feed.set('xmlns', 'http://www.w3.org/2005/Atom')

  title_elem = ElementTree.SubElement(feed, 'title')
  title_elem.text = title

  subtitle_elem = ElementTree.SubElement(feed, 'subtitle')
  subtitle_elem.text = subtitle

  id_elem = ElementTree.SubElement(feed, 'id')
  id_elem.text = link

  updated_elem = ElementTree.SubElement(feed, 'updated')
  updated_elem.text = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

  link_elem = ElementTree.SubElement(feed, 'link')
  link_elem.set('href', link)
  link_elem.set('rel', 'self')
  link_elem.set('type', 'application/atom+xml')

  for entry in entries:
    entry_elem = ElementTree.SubElement(feed, 'entry')

    title_elem = ElementTree.SubElement(entry_elem, 'title')
    title_elem.text = entry['title']

    link_elem = ElementTree.SubElement(entry_elem, 'link')
    link_elem.set('href', entry['link'])
    link_elem.set('rel', 'alternate')
    link_elem.set('type', 'text/html')

    id_elem = ElementTree.SubElement(entry_elem, 'id')
    id_elem.text = entry['link']

    published_elem = ElementTree.SubElement(entry_elem, 'published')
    published_elem.text = entry['published']

    updated_elem = ElementTree.SubElement(entry_elem, 'updated')
    updated_elem.text = entry['published']

    summary_elem = ElementTree.SubElement(entry_elem, 'summary')
    summary_elem.text = entry['summary']

  tree = ElementTree.ElementTree(feed)
  
  return tree

# Example usage
entries = [
    {
        'title': 'Blog Post 1',
        'link': 'https://example.com/post1',
        'published': '2023-11-22T10:00:00Z',
        'summary': 'This is the first blog post.'
    },
    # ... more entries
]

feed = generate_atom_feed(
    title='My Awesome Blog',
    subtitle='The latest news and updates',
    link='https://example.com/feed',
    entries=entries
)

# Write the feed to a file
feed.write('feed.xml', encoding='utf-8', xml_declaration=True)