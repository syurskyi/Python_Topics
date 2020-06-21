# Python Unittest
# unittest.mock � mock object library
# unittest.mock is a library for testing in Python.
# It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
# unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite.
# After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with.
# You can also specify return values and set needed attributes in the normal way.
# 
# Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel
# for creating unique objects.
# 
# Mock is very easy to use and is designed for use with unittest. Mock is based on the �action -> assertion� pattern instead of �record -> replay� used by
# many mocking frameworks.
#

#
# By default many of the protocol methods are required to return objects of a specific type.
# These methods are preconfigured with a default return value, so that they can be used without you having to do anything if you aren�t interested in the
# return value. 
# You can still set the return value manually if you want to change the default.
#

#
# For example:
# 

mock _ MagicMock()

__.(mock)

# OUTPUT: '1'

le.(mock)

# OUTPUT: '0'

li..(mock)

# OUTPUT: '[]'

object() __ mock

# OUTPUT: 'False'

# 
# The two equality methods, __eq__() and __ne__(), are special.
# They do the default equality comparison on identity, using the side_effect attribute, unless you change their return value to return something else:
# 

MagicMock() __ 3

# OUTPUT: 'False'

MagicMock() !_ 3

# OUTPUT: 'True'

mock _ MagicMock()
mock.__eq__.return_value _ T..

mock __ 3

# OUTPUT: 'True'

# 
# The return value of MagicMock.__iter__() can be any iterable object and isn�t required to be an iterator:
# 

mock _ MagicMock()
mock.__iter__.return_value _ ['a', 'b', 'c']

li..(mock)

# OUTPUT: '['a', 'b', 'c']'

li..(mock)

# OUTPUT: '['a', 'b', 'c']'

# 
# If the return value is an iterator, then iterating over it once will consume it and subsequent iterations will result in an empty list:
# 

mock.__iter__.return_value _ iter(['a', 'b', 'c'])

li..(mock)

# OUTPUT: '['a', 'b', 'c']'

li..(mock)

# OUTPUT: '[]'
