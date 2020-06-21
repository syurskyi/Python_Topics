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
# Using Mock:
# Mock Patching Methods
# Common uses for Mock objects include:
# > Patching methods
# > Recording method calls on objects
# 
# You might want to replace a method on an object to check that it is called with the correct arguments by another part of the system:
# 

real _ SomeClass()
real.method _ MagicMock(name_'method')

real.method(3, 4, 5, key_'value')

#
# This example tests that calling ProductionClass().method results in a call to the something method:
# 

c_ ProductionClass:
        ___ method
            something(1, 2, 3)

        ___ something  a, b, c
            p..

real _ ProductionClass()
real.something _ MagicMock()

real.method()

real.something.a_c_o_w..(1, 2, 3)
