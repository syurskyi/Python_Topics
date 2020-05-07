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
# assert_any_call(*args, **kwargs) 
# assert the mock has been called with the specified arguments.
# 
# The assert passes if the mock has ever been called, unlike assert_called_with() and assert_called_once_with() that only pass if the call is the most
# recent one, and in the case of assert_called_once_with() it must also be the only call.
# 

mock = Mock(return_value=None)
mock(1, 2, arg='thing')

mock('some', 'thing', 'else')

mock.assert_any_call(1, 2, arg='thing')

