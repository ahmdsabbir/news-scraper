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

    # Assuming published date is the same as updated date
    published_elem = ElementTree.SubElement(post, "published")
    published_elem.text = now

    category_elem = ElementTree.SubElement(post, "category", scheme="http://schemas.google.com/g/2005#kind")
    category_elem.text = "http://schemas.google.com/blogger/2008/kind#post"

    # Add labels as categories
    for label in labels:
        category_elem = ElementTree.SubElement(post, "category", scheme="http://www.blogger.com/atom/ns#")
        category_elem.text = label

    content_elem = ElementTree.SubElement(post, "content", type="html")
    content_elem.text = content

    # Add other elements like link, author if needed

    return post

def append_post_to_feed(feed_file, new_post):
    """
    Appends a new blog post element to an existing Blogger XML feed.

    Args:
        feed_file: The path to the existing Blogger XML feed file.
        new_post: The root element of the new blog post XML element.
    """

    try:
        tree = ElementTree.parse(feed_file)
        root = tree.getroot()
        # Look for the existing main `<feed>` element
        feed_element = root.find("feed")

        if feed_element is None:
            print("Error: The provided XML file doesn't contain a valid Blogger feed structure.")
            return

        # Append the new post element as a child of the existing `<feed>` element
        feed_element.append(new_post)

        tree.write(feed_file, encoding="utf-8", xml_declaration=True)
        print("New post appended successfully!")
    except Exception as e:
        print(f"Error appending post: {e}")

# Example usage
new_post_title = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
new_post_content = "<p>YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY</p>"
new_post_labels = ["python", "programming"]

new_post_element = create_blog_post_xml(new_post_title, new_post_content, new_post_labels)
append_post_to_feed("generated.xml", new_post_element)