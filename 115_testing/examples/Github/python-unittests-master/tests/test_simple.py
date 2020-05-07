import unittest
from app import simple


class IncrementTest(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(simple.increment(3), 4)
