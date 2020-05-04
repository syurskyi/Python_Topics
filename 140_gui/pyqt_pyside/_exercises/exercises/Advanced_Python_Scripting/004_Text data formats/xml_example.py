_____ xml.etree.ElementTree __ ET

path _ '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example5.xml'

tree _ ET.parse(path)
root _ tree.getroot
___ elem __ root.getchildren(
    print(elem.tag)
    print(elem.attrib)
    print(elem.t..)

___ readXml(root, ind_''
    ___ elem __ root.getchildren(
        print(ind, elem.tag)
        readXml(elem, ind+'  ')

readXml(root)

root _ ET.Element('root')
elem _ ET.SubElement(root, 'subElement')
elem.set('name', 'Max')
elem2 _ ET.SubElement(root, 'subElement2')
elem2.t.. _ 'SOME TEXT'

tree _ ET.ElementTree(root)
tree.w..(path)

____ xml.dom _____ minidom
xml _ minidom.parseString(ET.tostring(tree.getroot())).toprettyxml

w__ o..('/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example4.xml', 'w') __ f:
        f.w..(xml)