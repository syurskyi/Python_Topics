# namedtuple
# The standard tuple uses numerical indexes to access its members.

bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('Jane', 29, 'female')
print('\nField by index:', jane[0])

print('\nFields by index:')
for p in [ bob, jane ]:
    print('%s is a %d year old %s' % p)

# This makes tuples convenient containers for simple uses.
#
# $ python collections_tuple.py
#
# Representation: ('Bob', 30, 'male')
#
# Field by index: Jane
#
# Fields by index:
# Bob is a 30 year old male
# Jane is a 29 year old female

# On the other hand, remembering which index should be used for each value can lead to errors,
# especially if the tuple has a lot of fields and is constructed far from where it is used.
# A namedtuple assigns names, as well as the numerical index, to each member.

# Defining
# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance
# dictionaries. Each kind of namedtuple is represented by its own class, created by using the namedtuple()
# factory function. The arguments are the name of the new class and a string containing the names of the elements.

import collections

Person = collections.namedtuple('Person', 'name age gender')

print('Type of Person:', type(Person))

bob = Person(name='Bob', age=30, gender='male')
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29, gender='female')
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [ bob, jane ]:
    print('%s is a %d year old %s' % p)

# As the example illustrates, it is possible to access the fields of the namedtuple by name using dotted notation
# (obj.attr) as well as using the positional indexes of standard tuples.

# $ python collections_namedtuple_person.py
#
# Type of Person: <type 'type'>
#
# Representation: Person(name='Bob', age=30, gender='male')
#
# Field by name: Jane
#
# Fields by index:
# Bob is a 30 year old male
# Jane is a 29 year old female

# Invalid Field Names
# As the field names are parsed, invalid values cause ValueError exceptions.

import collections

try:
    collections.namedtuple('Person', 'name class age gender')
except ValueError, err:
    print err

try:
    collections.namedtuple('Person', 'name age gender age')
except ValueError, err:
    print err

# Names are invalid if they are repeated or conflict with Python keywords.
#
# $ python collections_namedtuple_bad_fields.py
#
# Type names and field names cannot be a keyword: 'class'
# Encountered duplicate field name: 'age'
#
# In situations where a namedtuple is being created based on values outside of the control of the programm
# (such as to represent the rows returned by a database query, where the schema is not known in advance),
# set the rename option to True so the fields are renamed.

import collections

with_class = collections.namedtuple('Person', 'name class age gender', rename=True)
print(with_class._fields)

two_ages = collections.namedtuple('Person', 'name age gender age', rename=True)
print(two_ages._fields)

# The field with name class becomes _1 and the duplicate age field is changed to _3.
#
# $ python collections_namedtuple_rename.py
#
# ('name', '_1', 'age', 'gender')
# ('name', 'age', 'gender', '_3')