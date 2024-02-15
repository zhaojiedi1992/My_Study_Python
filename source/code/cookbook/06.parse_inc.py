from lxml import etree
from io import  StringIO

class ElementHandler:
    def start(self, tag, attrib):
        self.current_tag = tag
        print("start tag:{}".format(self.current_tag))
    def end(self, tag):
        if tag == self.current_tag:
             print("end tag:{}".format(self.current_tag))
    def data(self, data):
        print('Data:', data)
    def close(self):
        print('End of document')
handler = ElementHandler()
parser = etree.XMLParser(target=handler)
xml_data = """
<root>
    <element key="value">Text content</element>
    <element key="another_value">Another text content</element>
</root>
"""
etree.parse(StringIO(xml_data), parser)