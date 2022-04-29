import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 3
from tempfile import TemporaryDirectory
from unittest import TestCase
class MyTest(TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
    def tearDown(self):
        self.test_dir.cleanup()
    # Test methods follow
