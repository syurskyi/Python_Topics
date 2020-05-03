_____ xml.etree.ElementTree __ ET

p _ '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example5.xml'

tree _ ET.parse(p)
root _ tree.getroot
elem _ root.find('element')
# print(elem.tag)
print(elem.attrib)
print(elem.t..)

# root = ET.Element('root2')
# elem = ET.SubElement(root, 'elem2')
# elem.set('name', 'Max')
# elem.text = 'SOME TEXT'
#
# tree = ET.ElementTree(root)
# p2 = '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
#     '004_Text data formats/example2.xml'
#
# tree.write(p2)
#
# from xml.dom import minidom
# xml = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
#
# f = open(p2, 'w')
# f.write(xml)
# f.close()

