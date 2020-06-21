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
# patch methods: start and stop.
# All the patchers have start() and stop() methods.
# These make it simpler to do patching in setUp methods or where you want to do multiple patches without nesting decorators or with statements.
# To use them call patch(), patch.object() or patch.dict() as normal and keep a reference to the returned patcher object.
# You can then call start() to put the patch in place and stop() to undo it.
# If you are using patch() to create a mock for you then it will be returned by the call to patcher.start.
# 

patcher _ patch('package.module.ClassName')

____ package ______ module

original _ module.ClassName

new_mock _ patcher.start()

a.. module.ClassName __ no. original
a.. module.ClassName __ new_mock

patcher.stop()

a.. module.ClassName __ original
a.. module.ClassName __ no. new_mock

# 
# A typical use case for this might be for doing multiple patches in the setUp method of a TestCase:
# 

c_ MyTest(T..

        ___ setUp
            patcher1 _ patch('package.module.Class1')
            patcher2 _ patch('package.module.Class2')

            MockClass1 _ patcher1.start()
            MockClass2 _ patcher2.start()

        ___ tearDown
            patcher1.stop()
            patcher2.stop()

        ___ test_something
            a.. package.module.Class1 __ MockClass1
            a.. package.module.Class2 __ MockClass2

MyTest('test_something').run()
 
#
# Caution:
# If you use this technique you must ensure that the patching is �undone� by calling stop.
# This can be fiddlier than you might think, because if an exception is raised in the setUp then tearDown is not called.
# unittest.TestCase.addCleanup() makes this easier:
# 

c_ MyTest(T..
        ___ setUp
            patcher _ patch('package.module.Class')

            MockClass _ patcher.start()
            addCleanup(patcher.stop)

        ___ test_something
            a.. package.module.Class __ MockClass
