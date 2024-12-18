from datetime import datetime
from xml.etree import ElementTree


def generate_blogger_xml(title, content, publish=True, labels=[]):
  """
  Generates an XML file compatible with Blogger import.

  Args:
      title: The title of the blog post.
      content: The content of the blog post (HTML format).
      publish: Whether to publish the post immediately (True) or schedule it (False).
      labels: A list of labels for the post.

  Returns:
      None
  """

  # Generate current date in Blogger format
  now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

  # Create the XML elements
  root = ElementTree.Element("entry", {"xmlns": "http://www.w3.org/2005/Atom"})
  title_element = ElementTree.SubElement(root, "title")
  title_element.text = title
  link_element = ElementTree.SubElement(root, "link", {"rel": "self", "href": ""})
  id_element = ElementTree.SubElement(root, "id")
  id_element.text = f"tag:{now}"
  updated_element = ElementTree.SubElement(root, "updated")
  updated_element.text = now
  author_element = ElementTree.SubElement(root, "author")
  name_element = ElementTree.SubElement(author_element, "name")
  # Replace with your author name
  name_element.text = "Your Name"
  content_element = ElementTree.SubElement(root, "content", {"type": "html"})
  content_element.text = content
  # Add labels if provided
  for label in labels:
    category_element = ElementTree.SubElement(root, "category", {"scheme": "http://www.blogger.com/atom/ns#"})
    category_element.text = label
  status_element = ElementTree.SubElement(root, "status")
  status_element.text = "publish" if publish else "draft"

  # Write the XML to a file
  tree = ElementTree.ElementTree(root)
  with open("blogger_post.xml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)

# Example usage
title = "My Blog Post Title"
content = """
  This is the content of my blog post. You can write your content in HTML format.
"""
labels = ["python", "programming"]
generate_blogger_xml(title, content, labels=labels)

print("Blogger XML file generated: blogger_post.xml")