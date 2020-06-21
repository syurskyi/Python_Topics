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
# Patch Decorators
# 

#
# Note:
# With patch() it matters that you patch objects in the namespace where they are looked up. This is normally straightforward, but for a quick guide read
# where to patch.
# 

#
# A common need in tests is to patch a class attribute or a module attribute, for example patching a builtin or patching a class in a module to test that it
# is instantiated. Modules and classes are effectively global, so patching on them has to be undone after the test or the patch will persist into other
# tests and cause hard to diagnose problems.
# mock provides three convenient decorators for this: patch(), patch.object() and patch.dict().
# patch takes a single string, of the form package.module.Class.attribute to specify the attribute you are patching.
# It also optionally takes a value that you want the attribute (or class or whatever) to be replaced with.
# �patch.object� takes an object and the name of the attribute you would like patched, plus optionally the value to patch it with.
#

# 
# patch.object:
# 

original _ SomeClass.attribute

?p...object(SomeClass, 'attribute', sentinel.attribute)

      ___ test(
         a.. SomeClass.attribute __ sentinel.attribute

      test()
         a.. SomeClass.attribute __ original
 

?p..('package.module.attribute', sentinel.attribute)
     ___ test(

        ____ package.module ______ attribute
          a.. attribute __ sentinel.attribute

     test()
 
#
# If you are patching a module (including builtins) then use patch() instead of patch.object():
# 

mock _ MagicMock(return_value_sentinel.file_handle)
       w__ patch('builtins.open', mock

        handle _ o..('filename', _

mock.a_c_w..('filename', _

a.. handle __ sentinel.file_handle, "incorrect file handle returned"

# 
# The module name can be �dotted�, in the form package.module if needed:
# 

?p..('package.module.ClassName.attribute', sentinel.attribute)

    ___ test(
        ____ package.module ______ ClassName

        a.. ClassName.attribute __ sentinel.attribute

    test()
 
#
# A nice pattern is to actually decorate test methods themselves:
# 

c_ MyTest?.?

       ?p...object(SomeClass, 'attribute', sentinel.attribute)

        ___ test_something
           aE..(SomeClass.attribute, sentinel.attribute)

original _ SomeClass.attribute

MyTest('test_something').test_something()

a.. SomeClass.attribute __ original
 
#
# If you want to patch with a Mock, you can use patch() with only one argument (or patch.object() with two arguments).
# The mock will be created for you and passed into the test function / method:
# 

c_ MyTest?.?

        ?p...object(SomeClass, 'static_method')

        ___ test_something  mock_method
            SomeClass.static_method()

           mock_method.a_c_w..()

MyTest('test_something').test_something()

# 
# You can stack up multiple patch decorators using this pattern:
# 

c_ MyTest?.?

?p..('package.module.ClassName1')
?p..('package.module.ClassName2')

        ___ test_something  MockClass2, MockClass1
            assertIs(package.module.ClassName1, MockClass1)

            assertIs(package.module.ClassName2, MockClass2)

MyTest('test_something').test_something()

# 
# When you nest patch decorators the mocks are passed in to the decorated function in the same order they applied (the normal Python order that decorators
# are applied).
# This means from the bottom up, so in the example above the mock for test_module.ClassName2 is passed in first.
# There is also patch.dict() for setting values in a dictionary just during a scope and restoring the dictionary to its original state when the test ends:
# 

foo _ {'key': 'value'}
original _ foo.copy()

   w__ patch.dict(foo, {'newkey': 'newvalue'}, clear_True
        a.. foo __ {'newkey': 'newvalue'}

a.. foo __ original

# 
# patch, patch.object and patch.dict can all be used as context managers.
#

# 
# Where you use patch() to create a mock for you, you can get a reference to the mock using the �as� form of the with statement:
# 

c_ ProductionClass:
        ___ method
            p..

    w__ patch.object(ProductionClass, 'method') __ mock_method:
        mock_method.return_value _ N..

        real _ ProductionClass()
        real.method(1, 2, 3)

mock_method.a_c_w..(1, 2, 3)
 
#
# As an alternative patch, patch.object and patch.dict can be used as class decorators.
# When used in this way it is the same as applying the decorator individually to every method whose name starts with �test�.
#
