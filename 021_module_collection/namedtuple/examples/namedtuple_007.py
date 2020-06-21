# The namedtuple()
# The namedtuple() returns a tuple with names for each position in the tuple. One of the biggest problems
# with ordinary tuples is that you have to remember the index of each field of a tuple object.
# This is obviously difficult. The namedtuple was introduced to solve this problem.
# Import namedtuple
# Before using namedtuple, you have to import it from the collections module.

from collections import namedtuple

# Create a namedtuple

from collections import namedtuple

Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)

# Output:
# Student(fname='John', lname='Clarke', age='13')

# In this example, a namedtuple object Student has been declared. You can access the fields of any instance
# of a Student class by the defined field name.
# Creating a namedtuple Using List
# The namedtuple() function requires each value to be passed to it separately.
# Instead, you can use _make() to create a namedtuple instance with a list. Check the following code:

s2 = Student._make(['Adam','joe','18'])
print(s2)

# Output:
# Student(fname='Adam', lname='joe', age='18')

# Create a New Instance Using Existing Instance
# The _asdict() function can be used to create an OrderedDict instance from an existing instance.

s2 = s1._asdict()
print(s2)

# Output:
# OrderedDict([('fname', 'John'), ('lname', 'Clarke'), ('age', '13')])

# Changing Field Values with _replace() Function
# To change the value of a field of an instance, the _replace() function is used. Remember that, _replace()
# function creates a new instance. It does not change the value of existing instance.

s2 = s1._replace(age='14')
print(s1)
print(s2)

# Output:
# Student(fname='John', lname='Clarke', age='13')
# Student(fname='John', lname='Clarke', age='14')
