# Python Regression Testing
# test � Regression tests package for Python
# 
##########################################################################################################################################################
#
# NOTE:
#
# The test package is meant for internal use by Python only. It is documented for the benefit of the core developers of Python.
# Any use of this package outside of Python�s standard library is discouraged as code mentioned here can change or be removed without notice between
# releases of Python.
#
########################################################################################################################################################## 
#
# The test package contains all regression tests for Python as well as the modules test.support and test.regrtest.
# test.support is used to enhance your tests while test.regrtest drives the testing suite.
# 
# Each module in the test package whose name starts with test_ is a testing suite for a specific module or feature.
# All new tests should be written using the unittest or doctest module. Some older tests are written using a �traditional� testing style that compares
# output printed to sys.stdout; this style of test is considered deprecated.
#

#
# test.support.captured_stdin()
# test.support.captured_stdout()
# test.support.captured_stderr()
# A context managers that temporarily replaces the named stream with io.StringIO object.
#

# 
# Example use with output streams:
# 

w__ captured_stdout() __ stdout, captured_stderr() __ stderr:
    print("hello")

    print("error", file_sys.stderr)

a.. stdout.getvalue() __ "hello\n"
a.. stderr.getvalue() __ "error\n"
 
#
# Example use with input stream:
# 

w__ captured_stdin() __ stdin:
    stdin.write('hello\n')

    stdin.seek(0)

    # call test code that consumes from sys.stdin

    captured _ __..()

aE..(captured, "hello")
