import xml.etree.ElementTree as ET

def create_blogger_post_xml():
    # Create the root element 'feed'
    feed = ET.Element('feed', {
        'xmlns': 'http://www.w3.org/2005/Atom',
        'xmlns:openSearch': 'http://a9.com/-/spec/opensearch/1.1/',
        'xmlns:gd': 'http://schemas.google.com/g/2005',
        'xmlns:thr': 'http://purl.org/syndication/thread/1.0',
        'xmlns:georss': 'http://www.georss.org/georss'
    })

    # Add the required elements under 'feed'
    ET.SubElement(feed, 'id').text = 'tag:blogger.com,1999:blog-1234567890123456789'
    ET.SubElement(feed, 'updated').text = '2023-10-25T12:00:00.000Z'
    ET.SubElement(feed, 'title', {'type': 'text'}).text = 'Your Blog Title'

    # Create an 'entry' element
    entry = ET.SubElement(feed, 'entry')

    # Add sub-elements to the 'entry'
    ET.SubElement(entry, 'id').text = 'tag:blogger.com,1999:blog-1234567890123456789.post-1234567890123456789'
    ET.SubElement(entry, 'published').text = '2023-10-25T12:00:00.000Z'
    ET.SubElement(entry, 'updated').text = '2023-10-25T12:00:00.000Z'
    ET.SubElement(entry, 'category', {
        'scheme': 'http://www.blogger.com/atom/ns#',
        'term': 'Uncategorized'
    })
    ET.SubElement(entry, 'title', {'type': 'text'}).text = 'Example Post'
    
    # Create content element with CDATA section
    content = ET.SubElement(entry, 'content', {'type': 'html'})
    content.text = ET.CDATA('<p>This is the content of your example blog post. You can include HTML tags here.</p>')

    # Author info
    author = ET.SubElement(entry, 'author')
    ET.SubElement(author, 'name').text = 'Your Name'
    ET.SubElement(author, 'email').text = 'your.email@example.com'

    # Generate the XML tree and write to a file
    tree = ET.ElementTree(feed)
    ET.indent(tree, space="  ", level=0)  # Pretty print with indentation for Python 3.9+

    with open('blogger_post.xml', 'wb') as xml_file:
        tree.write(xml_file, encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    create_blogger_post_xml()
    print("XML file 'blogger_post.xml' generated successfully.")