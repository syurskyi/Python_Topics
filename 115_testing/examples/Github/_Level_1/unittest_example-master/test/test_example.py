import unittest

# from typing import ...

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
def setUpModule() -> None:
    """called once, before anything else in this module"""
    print("In SetUpModule()...(module-level fixture)")


def tearDownModule() -> None:
    """called once, after everything else in this module"""
    print("In tearDownModule()...(module-level fixture)")


# Test class
# ------------------------------------------------------------
class TestClassExample(unittest.TestCase):

    # Class-level fixtures. Require the classmethod decorator
    # -----------------------------------------------------------
    @classmethod
    def setUpClass(cls) -> None:
        """called once, at the beginning of the class testing"""
        print("In setUpClass()...(class-level fixture)")

    @classmethod
    def tearDownClass(cls) -> None:
        """called once, once all tests have been done, if setUpClass succesfull"""
        print("In tearDownClass")

    # Method-level fixtures
    # -----------------------------------------------------------
    def setUp(self) -> None:
        """called before every test method"""
        print("In setUp()...")

    def tearDown(self) -> None:
        """called after every test method"""

    # Test case related functions
    # -----------------------------------------------------------
    # Assert methods available
    # https://docs.python.org/3/library/unittest.html#assert-methods

    # Test cases
    def test_case01(self):
        print(self.id())  # Print module, class and method name, to ease test output analysis
        self.assertEqual(True, False)

    def test_case02(self):
        print(self.id())
        self.assertEqual(True, True)

    def test_case03(self):
        print(self.id())
        self.assertNotEqual(True, False)

if __name__ == '__main__':
    unittest.main()
