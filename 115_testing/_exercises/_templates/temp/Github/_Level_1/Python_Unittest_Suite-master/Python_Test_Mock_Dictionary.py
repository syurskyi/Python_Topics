# Python Test Mock
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
# Mocking a dictionary with MagicMock:
# You may want to mock a dictionary, or other container object, recording all access to it whilst having it still behave like a dictionary.
# We can do this with MagicMock, which will behave like a dictionary, and using side_effect to delegate dictionary access to a real underlying dictionary
# that is under our control.
# When the __getitem__() and __setitem__() methods of our MagicMock are called (normal dictionary access) then side_effect is called with the key (and in
# the case of __setitem__ the value too).
# We can also control what is returned.
# 

#
# After the MagicMock has been used we can use attributes like call_args_list to assert about how the dictionary was used:
# 

my_dict _ {'a': 1, 'b': 2, 'c': 3}

    ___ getitem(name
         r_ my_dict[name]

    ___ setitem(name, val
        my_dict[name] _ val

mock _ MagicMock()
mock.__getitem__.side_effect _ getitem

mock.__setitem__.side_effect _ setitem
 

#
# Note:
# An alternative to using MagicMock is to use Mock and only provide the magic methods you specifically want:
# 

mock _ Mock()

mock.__getitem__ _ Mock(side_effect_getitem)
mock.__setitem__ _ Mock(side_effect_setitem)

# 
# A third option is to use MagicMock but passing in dict as the spec (or spec_set) argument so that the MagicMock created only has dictionary magic methods
# available:
# 

mock _ MagicMock(spec_set_dict)

mock.__getitem__.side_effect _ getitem
mock.__setitem__.side_effect _ setitem
 
#
# With these side effect functions in place, the mock will behave like a normal dictionary but recording the access.
# It even raises a KeyError if you try to access a key that doesn�t exist.
# 

mock['a']

# OUTPUT: '1'

mock['c']

# OUTPUT: '3'

mock['d']

mock['b'] _ 'fish'

mock['d'] _ 'eggs'

mock['b']

# OUTPUT: 'fish'

mock['d']

# OUTPUT: 'eggs'

# 
# After it has been used you can make assertions about the access using the normal mock methods and attributes:
# 

mock.__getitem__.call_args_list

# OUTPUT: '[call('a'), call('c'), call('d'), call('b'), call('d')]'

mock.__setitem__.call_args_list

# OUTPUT: '[call('b', 'fish'), call('d', 'eggs')]'

my_dict

# OUTPUT: '{'a': 1, 'c': 3, 'b': 'fish', 'd': 'eggs'}'
