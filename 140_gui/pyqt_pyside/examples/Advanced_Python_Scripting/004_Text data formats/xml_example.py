import xml.etree.ElementTree as ET

path = '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example5.xml'

tree = ET.parse(path)
root = tree.getroot()
for elem in root.getchildren():
    print(elem.tag)
    print(elem.attrib)
    print(elem.text)

def readXml(root, ind=''):
    for elem in root.getchildren():
        print(ind, elem.tag)
        readXml(elem, ind+'  ')

readXml(root)

root = ET.Element('root')
elem = ET.SubElement(root, 'subElement')
elem.set('name', 'Max')
elem2 = ET.SubElement(root, 'subElement2')
elem2.text = 'SOME TEXT'

tree = ET.ElementTree(root)
tree.write(path)

from xml.dom import minidom
xml = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()

with open('/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example4.xml', 'w') as f:
        f.write(xml)