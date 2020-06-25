# # namedtuple
# # The standard tuple uses numerical indexes to access its members.
#
# bob _ 'Bob' 30 'male'
# print 'Representation:' b..
#
# jane _ 'Jane', 29, 'female'
# print '\nField by index:' jane 0
#
# print'\nFields by index:'
# ___ p i_ | bob jane
#     print '/ is a / year old /' / p
#
# # This makes tuples convenient containers for simple uses.
# #
# # $ python collections_tuple.py
# #
# # Representation: ('Bob', 30, 'male')
# #
# # Field by index: Jane
# #
# # Fields by index:
# # Bob is a 30 year old male
# # Jane is a 29 year old female
#
# # On the other hand, remembering which index should be used for each value can lead to errors,
# # especially if the tuple has a lot of fields and is constructed far from where it is used.
# # A namedtuple assigns names, as well as the numerical index, to each member.
#
# # Defining
# # namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance
# # dictionaries. Each kind of namedtuple is represented by its own class, created by using the namedtuple()
# # factory function. The arguments are the name of the new class and a string containing the names of the elements.
#
# ______ c___
#
# Person = c___.n..t.. 'Person' 'name age gender'
#
# print 'Type of Person:', ty.. P..
#
# bob _ P.. name_'Bob' age_30 gender_'male'
# print '\nRepresentation:' b..
#
# jane _ P... name_'Jane' age_29 gender_'female'
# print '\nField by name:' j__.na..
#
# print('\nFields by index:')
# ___ p i_ |bob jane
#     print('/ is a / year old /' / p
#
# # As the example illustrates, it is possible to access the fields of the namedtuple by name using dotted notation
# # (obj.attr) as well as using the positional indexes of standard tuples.
#
# # $ python collections_namedtuple_person.py
# #
# # Type of Person: <type 'type'>
# #
# # Representation: Person(name='Bob', age=30, gender='male')
# #
# # Field by name: Jane
# #
# # Fields by index:
# # Bob is a 30 year old male
# # Jane is a 29 year old female
#
# # Invalid Field Names
# # As the field names are parsed, invalid values cause ValueError exceptions.
#
# ____ c...
#
# t__
#     c___.n..t.. 'Person' 'name class age gender'
# e____ V..E.. e..
#     print e..
#
# t__
#     c___.n..t.. 'Person' 'name age gender age'
# e______ V..E.. e..
#     print e..
#
# # Names are invalid if they are repeated or conflict with Python keywords.
# #
# # $ python collections_namedtuple_bad_fields.py
# #
# # Type names and field names cannot be a keyword: 'class'
# # Encountered duplicate field name: 'age'
# #
# # In situations where a namedtuple is being created based on values outside of the control of the programm
# # (such as to represent the rows returned by a database query, where the schema is not known in advance),
# # set the rename option to True so the fields are renamed.
#
# _______ c__
#
# with_class _ c___.n..t.. 'Person' 'name class age gender', re.._T..
# print w._c.._fi..
#
# two_ages _ c___.n..t.. 'Person' 'name age gender age', re.._T..
# print t.._a__._fi..
#
# # The field with name class becomes _1 and the duplicate age field is changed to _3.
# #
# # $ python collections_namedtuple_rename.py
# #
# # ('name', '_1', 'age', 'gender')
# # ('name', 'age', 'gender', '_3')