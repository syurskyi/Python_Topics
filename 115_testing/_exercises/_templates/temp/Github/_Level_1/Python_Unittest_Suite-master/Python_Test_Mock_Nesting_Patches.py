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
# Nesting Patches:
# Using patch as a context manager is nice, but if you do multiple patches you can end up with nested with statements indenting further and further to the
# right:
# 

c_ MyTest(T..

        ___ test_foo

            w__ patch('mymodule.Foo') __ mock_foo:

                w__ patch('mymodule.Bar') __ mock_bar:

                    w__ patch('mymodule.Spam') __ mock_spam:

                        a.. mymodule.Foo __ mock_foo

                        a.. mymodule.Bar __ mock_bar

                       a.. mymodule.Spam __ mock_spam

original _ mymodule.Foo

MyTest('test_foo').test_foo()

a.. mymodule.Foo __ original

# 
# With unittest cleanup functions and the patch methods: start and stop we can achieve the same effect without the nested indentation.
#
# A simple helper method, create_patch, puts the patch in place and returns the created mock for us:
# 

c_ MyTest(T..

       ___ create_patch  name
            patcher _ patch(name)

            thing _ patcher.start()

            addCleanup(patcher.stop)

            r_ thing

        ___ test_foo
            mock_foo _ create_patch('mymodule.Foo')

            mock_bar _ create_patch('mymodule.Bar')
            mock_spam _ create_patch('mymodule.Spam')

            a.. mymodule.Foo __ mock_foo

            a.. mymodule.Bar __ mock_bar
            a.. mymodule.Spam __ mock_spam

original _ mymodule.Foo

MyTest('test_foo').run()

a.. mymodule.Foo __ original
