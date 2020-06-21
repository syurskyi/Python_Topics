______ u__

# from typing ______ ...

# Example code to organize the unit testing of a class following xUnit philosophy with 'unittest'
# Designed following chapters 3 and 6 of "Python Unit Test Automation" - Ashwin Pajankar
# It has been written in a typed manner (PEP 484) (hence, only fully work as of Python 3.6)
# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b

# 'Fixture' (ENG) -> 'Accessori' (CAT)
# Test fixtures : set of sterps performed before and after the tests
# There are module-level, class-level and function-level fixtures
# module-level: executed once at the beginning/end of the module testing.
# class-level: executed once at the beginning/end of the class testing.
# function-level: executed before/after every test method in the test class
# Notice that function fixtures does not follow PEP8 python naming style !!

# Module-level fixtures
# -----------------------------------------------------------
___ setUpModule()  N..:
    """called once, before anything else in this module"""
    print("In SetUpModule()...(module-level fixture)")


___ tearDownModule()  N..:
    """called once, after everything else in this module"""
    print("In tearDownModule()...(module-level fixture)")


# Test class
# ------------------------------------------------------------
c_ TestClassExample?.?

    # Class-level fixtures. Require the classmethod decorator
    # -----------------------------------------------------------
    ??
    ___ setUpClass ___)  N..:
        """called once, at the beginning of the class testing"""
        print("In setUpClass()...(class-level fixture)")

    ??
    ___ tearDownClass ___)  N..:
        """called once, once all tests have been done, if setUpClass succesfull"""
        print("In tearDownClass")

    # Method-level fixtures
    # -----------------------------------------------------------
    ___ setUp(self)  N..:
        """called before every test method"""
        print("In setUp()...")

    ___ tearDown(self)  N..:
        """called after every test method"""

    # Test case related functions
    # -----------------------------------------------------------
    # Assert methods available
    # https://docs.python.org/3/library/unittest.html#assert-methods

    # Test cases
    ___ test_case01
        print(id())  # Print module, class and method name, to ease test output analysis
        aE..(T.., F..)

    ___ test_case02
        print(id())
        aE..(T.., T..)

    ___ test_case03
        print(id())
        aNE..(T.., F..)

__ _____ __ _____
    ?.?
