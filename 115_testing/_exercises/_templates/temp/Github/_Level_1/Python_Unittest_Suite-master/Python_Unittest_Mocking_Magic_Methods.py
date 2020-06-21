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
# Mocking Magic Methods:
# Mock supports mocking the Python protocol methods, also known as �magic methods�.
# This allows mock objects to replace containers or other objects that implement Python protocols.
# Because magic methods are looked up differently from normal methods, this support has been specially implemented. This means that only specific magic
# methods are supported.
#
# The supported list includes almost all of them. If there are any missing that you need please let us know.
# 

#
# You mock magic methods by setting the method you are interested in to a function or a mock instance.
# If you are using a function then it must take self as the first argument.
# 

___ -s
        r_ 'fooble'

mock _ Mock()
mock.-s _ -s

st.(mock)

# OUTPUT: 'fooble'
 

mock _ Mock()
mock.-s _ Mock()

mock.-s.return_value _ 'fooble'

st.(mock)

# OUTPUT: 'fooble'
 

mock _ Mock()
mock.__iter__ _ Mock(return_value_iter([]))

li..(mock)

# OUTPUT: '[]'

# 
# One use case for this is for mocking objects used as context managers in a with statement:
# 

mock _ Mock()
mock.__enter__ _ Mock(return_value_'foo')

mock.__exit__ _ Mock(return_value_False)

w__ mock __ m:
        a.. m __ 'foo'

mock.__enter__.a_c_w..()

mock.__exit__.a_c_w..(N.., N.., N..)
