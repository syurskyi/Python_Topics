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

# patch.dict.
# patch.dict(in_dict, values=(), clear=False, **kwargs). 
# Patch a dictionary, or dictionary like object, and restore the dictionary to its original state after the test.
# 
# in_dict can be a dictionary or a mapping like container. If it is a mapping then it must at least support getting, setting and deleting items plus
# iterating over keys.
# in_dict can also be a string specifying the name of the dictionary, which will then be fetched by importing it.
# values can be a dictionary of values to set in the dictionary. values can also be an iterable of (key, value) pairs.
#
# If clear is true then the dictionary will be cleared before the new values are set.
# 
# patch.dict() can also be called with arbitrary keyword arguments to set values in the dictionary.
# 
# patch.dict() can be used as a context manager, decorator or class decorator. When used as a class decorator patch.dict() honours patch.TEST_PREFIX for
# choosing which methods to wrap.
# 
# patch.dict() can be used to add members to a dictionary, or simply let a test change a dictionary, and ensure the dictionary is restored when the test
# ends.
# 

foo _ {}

w__ patch.dict(foo, {'newkey': 'newvalue'}
        a.. foo __ {'newkey': 'newvalue'}

a.. foo __ {}
 

______ __

w__ patch.dict('os.environ', {'newkey': 'newvalue'}
        print(__.environ['newkey'])


# OUTPUT: 'newvalue'

a.. 'newkey' no. __ __.environ

# 
# Keywords can be used in the patch.dict() call to set values in the dictionary:
# 

mymodule _ MagicMock()
mymodule.function.return_value _ 'fish'

w__ patch.dict('sys.modules', mymodule_mymodule
        ______ mymodule
 
       mymodule.function('some', 'args')

# OUTPUT: 'fish'
 
#
# patch.dict() can be used with dictionary like objects that aren�t actually dictionaries.
# At the very minimum they must support item getting, setting, deleting and either iteration or membership test.
# This corresponds to the magic methods __getitem__(), __setitem__(), __delitem__() and either __iter__() or __contains__().
# 

c_ Container:
        ___  -
            values _ {}

        ___ __getitem__  name
            r_ values[name]

        ___ __setitem__  name, value
            values[name] _ value

        ___ __delitem__  name
            del values[name]

        ___ __iter__
            r_ iter(values)

thing _ Container()
thing['one'] _ 1

w__ patch.dict(thing, one_2, two_3
        a.. thing['one'] __ 2

       a.. thing['two'] __ 3

a.. thing['one'] __ 1
a.. li..(thing) __ ['one']
