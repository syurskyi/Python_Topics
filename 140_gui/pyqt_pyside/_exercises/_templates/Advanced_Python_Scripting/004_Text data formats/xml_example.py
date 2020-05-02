_____ xml.etree.ElementTree as ET

path _ '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example5.xml'

tree _ ET.parse(path)
root _ tree.getroot()
for elem in root.getchildren(
    print(elem.tag)
    print(elem.attrib)
    print(elem.t..)

___ readXml(root, ind_''
    for elem in root.getchildren(
        print(ind, elem.tag)
        readXml(elem, ind+'  ')

readXml(root)

root _ ET.Element('root')
elem _ ET.SubElement(root, 'subElement')
elem.set('name', 'Max')
elem2 _ ET.SubElement(root, 'subElement2')
elem2.t.. _ 'SOME TEXT'

tree _ ET.ElementTree(root)
tree.write(path)

____ xml.dom _____ minidom
xml _ minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()

with open('/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example4.xml', 'w') as f:
        f.write(xml)