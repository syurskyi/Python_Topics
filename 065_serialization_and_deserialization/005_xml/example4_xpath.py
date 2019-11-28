from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()

# search value
first_names = root.findall('./person[@pk="21"]/first_name')
last_names = root.findall('person[@pk="21"]/last_name')
ages = root.findall('person/[@pk="21"]/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

last_name = root.find('./person/age/..[@pk][1]/first_name').text
print(last_name)

last_name = root.find('./person/age/..[@pk][2]/first_name').text
print(last_name)

last_name = root.find('./person/age/..[@pk][3]/first_name').text
print(last_name)
