import unittest
from app import simple


c_ IncrementTest(unittest.TestCase):
    ___ test_increment(self):
        self.assertEqual(simple.increment(3), 4)
