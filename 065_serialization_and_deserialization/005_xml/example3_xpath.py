from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()
children = root.getchildren()

for student_data in children:
    print('PK: ', (student_data.attrib, student_data.get('pk')))
    print('{} {} {}'.format(
        student_data.find('./first_name').text,
        student_data.find('./last_name').text,
        student_data.find('./age').text
    ))

# search value
first_names = root.findall('./person/first_name')
last_names = root.findall('./person/last_name')
ages = root.findall('./person/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

for student_data in children:
    print("PK: ", student_data.attrib)
    for child in student_data:
        print('{}: {}'.format(child.tag, child.text))
