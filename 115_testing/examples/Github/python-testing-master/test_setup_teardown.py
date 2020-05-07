import unittest
from unittest import TestCase


class TestSetUpAndTearDown(TestCase):
    """Showcase for a test with setUp and tearDown methods"""

    important_value = None

    # Is run before each test. Should be used to create clean condition for each test.
    def setUp(self):
        self.important_value = 1337

    # Is run after each test. Mostly used for closing connections/files or clean up stuff.
    def tearDown(self):
        self.important_value = None

    def test_value_after_setup(self):
        self.assertEqual(1337, self.important_value)


# build in main method to run all tests in this class
if __name__ == '__main__':
    unittest.main()
