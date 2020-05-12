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
# Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used.
# You can configure them, to specify return values or limit what attributes are available, and then make assertions about how they have been used:
# 

____ u__.m.. ______ MagicMock

thing _ ProductionClass()
thing.method _ MagicMock(return_value_3)

thing.method(3, 4, 5, key_'value')

# OUTPUT: '3'

thing.method.a_c_w..(3, 4, 5, key_'value')

# 
# side_effect allows you to perform side effects, including raising an exception when a mock is called:
# 

mock _ Mock(side_effect_KeyError('foo'))
mock()

values _ {'a': 1, 'b': 2, 'c': 3}

___ side_effect(arg
        r_ values[arg]

mock.side_effect _ side_effect
mock('a'), mock('b'), mock('c')

# OUTPUT: '(1, 2, 3)'

mock.side_effect _ [5, 4, 3, 2, 1]
mock(), mock(), mock()

# OUTPUT: '(5, 4, 3)'
