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
# Nesting Patch Decorators:
# If you want to perform multiple patches then you can simply stack up the decorators.
#

# 
# You can stack up multiple patch decorators using this pattern:
# 

?p...object(SomeClass, 'class_method')
?p...object(SomeClass, 'static_method')

___ test(mock1, mock2
        a.. SomeClass.static_method __ mock1
        a.. SomeClass.class_method __ mock2

        SomeClass.static_method('foo')
        SomeClass.class_method('bar')

        r_ mock1, mock2

mock1, mock2 _ test()
mock1.a_c_o_w..('foo')

mock2.a_c_o_w..('bar')

# 
# Note that the decorators are applied from the bottom upwards.
# This is the standard way that Python applies decorators.
# The order of the created mocks passed into your test function matches this order.
#