# # The namedtuple()
# # The namedtuple() returns a tuple with names for each position in the tuple. One of the biggest problems
# # with ordinary tuples is that you have to remember the index of each field of a tuple object.
# # This is obviously difficult. The namedtuple was introduced to solve this problem.
# # ____ namedtuple
# # Before using namedtuple, you have to ____ it from the collections module.
#
# f__ c.. ____ n..t..
#
# # Create a namedtuple
#
# f__ c.. ____ n..t..
#
# Student n..t.. n..t.. 'Student' 'fname, lname, age'
# s1 _ S..'John' 'Clarke' '13'
# print s1.f..
#
# # Output:
# # Student(fname='John', lname='Clarke', age='13')
#
# # In this example, a namedtuple object Student has been declared. You can access the fields of any instance
# # of a Student class by the defined field name.
# # Creating a namedtuple Using List
# # The namedtuple() function requires each value to be passed to it separately.
# # Instead, you can use _make() to create a namedtuple instance with a list. Check the following code:
#
# s2 = S__._ma.. 'Adam' 'joe' '18'
# print s2
#
# # Output:
# # Student(fname='Adam', lname='joe', age='18')
#
# # Create a New Instance Using Existing Instance
# # The _asdict() function can be used to create an OrderedDict instance from an existing instance.
#
# s2 _ s1._asdi.
# print(s2)
#
# # Output:
# # OrderedDict([('fname', 'John'), ('lname', 'Clarke'), ('age', '13')])
#
# # Changing Field Values with _replace() Function
# # To change the value of a field of an instance, the _replace() function is used. Remember that, _replace()
# # function creates a new instance. It does not change the value of existing instance.
#
# s2 = s1._rep.. age_'14'
# print(s1)
# print(s2)
#
# # Output:
# # Student(fname='John', lname='Clarke', age='13')
# # Student(fname='John', lname='Clarke', age='14')
