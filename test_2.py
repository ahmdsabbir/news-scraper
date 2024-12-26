import xml.etree.ElementTree as ET

def generate_atom_feed(title, content):
    # Root entry element
    entry = ET.Element("entry")

    # ID
    id_element = ET.SubElement(entry, "id")
    id_element.text = "tag:blogger.com,1999:blog-5968071689632345895.post-207570408380315315"

    # Published
    published_element = ET.SubElement(entry, "published")
    published_element.text = "2024-18-02T06:29:00.000-08:00"

    # Updated
    updated_element = ET.SubElement(entry, "updated")
    updated_element.text = "2024-18-02T06:29:46.120-08:00"

    # Categories
    category1 = ET.SubElement(entry, "category")
    category1.set("scheme", "http://schemas.google.com/g/2005#kind")
    category1.set("term", "http://schemas.google.com/blogger/2008/kind#post")

    category2 = ET.SubElement(entry, "category")
    category2.set("scheme", "http://www.blogger.com/atom/ns#")
    category2.set("term", "Technology")

    # Title
    title_element = ET.SubElement(entry, "title")
    title_element.set("type", "text")
    title_element.text = title

    # Content
    content_element = ET.SubElement(entry, "content")
    content_element.set("type", "html")
    content_element.text = content

    # Links
    link_edit = ET.SubElement(entry, "link")
    link_edit.set("rel", "edit")
    link_edit.set("type", "application/atom+xml")
    link_edit.set("href", "https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315")

    link_self = ET.SubElement(entry, "link")
    link_self.set("rel", "self")
    link_self.set("type", "application/atom+xml")
    link_self.set("href", "https://www.blogger.com/feeds/5968071689632345895/posts/default/207570408380315315")

    link_alternate = ET.SubElement(entry, "link")
    link_alternate.set("rel", "alternate")
    link_alternate.set("type", "text/html")
    link_alternate.set("href", "https://winttech.blogspot.com/2024/12/blog-post.html")
    link_alternate.set("title", "দেশের বাজারে ২৫০ সিসির নতুন দুই মোটরসাইকেল, দাম কত")

    # Author
    author_element = ET.SubElement(entry, "author")

    author_name = ET.SubElement(author_element, "name")
    author_name.text = "Khobor Dunia"

    author_uri = ET.SubElement(author_element, "uri")
    author_uri.text = "https://www.blogger.com/profile/06693327077864093576"

    author_email = ET.SubElement(author_element, "email")
    author_email.text = "noreply@blogger.com"

    author_image = ET.SubElement(author_element, "gd:image")
    author_image.set("rel", "http://schemas.google.com/g/2005#thumbnail")
    author_image.set("width", "35")
    author_image.set("height", "35")
    author_image.set("src", "//www.blogger.com/img/blogger_logo_round_35.png")

    # Convert to string
    xml_str = ET.tostring(entry, encoding="unicode")
    return xml_str

# Example usage
if __name__ == "__main__":
    title = "New Test Title"
    content = "<p>This is new test content</p>"
    atom_feed = generate_atom_feed(title, content)
    print(atom_feed)
