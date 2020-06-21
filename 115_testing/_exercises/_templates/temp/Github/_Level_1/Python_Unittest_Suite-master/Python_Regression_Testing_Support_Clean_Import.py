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
# class test.support.CleanImport(*module_names): 
# A context manager to force ______ to return a new module reference.
# This is useful for testing module-level behaviors, such as the emission of a DeprecationWarning on ______.
#
# Example usage:
# 

w__ CleanImport('foo'

       importlib.import_module('foo')  # New reference.
