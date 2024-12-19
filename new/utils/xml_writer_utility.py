from xml.etree import ElementTree
from datetime import datetime

class XMLWriter:
    def __init__(self, output: str, root: str):
        self.output_fname = output
        self.root_fname = root

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

# # Example usage
# new_post = create_blog_post_xml(
#     title="My New Blog Post",
#     content="<p>This is the content of my new blog post.</p>",
#     labels=["python", "programming"]
# )

# Example usage
# Assuming you have a Blogger XML feed named 'my_blog_feed.xml'
# append_post_to_feed("base.xml", new_post)