# We can use the xml.etree.ElementTree module which is a simple 
# API for parsing and creating XML data. 
# https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

tree = ET.parse('sampleXML.xml')
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# While the parsing is very simple, remember that there are many rules regarding
# valid XML. Using ElementTree allows us to extract data without
# worrying about the rules of XML syntax