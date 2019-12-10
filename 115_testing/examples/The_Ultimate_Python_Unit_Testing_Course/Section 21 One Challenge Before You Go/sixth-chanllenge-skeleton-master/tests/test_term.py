"""
    This is just an example to get you started.
    1- Test for None values.
    2- Make sure that the Term class constructor only takes numbers.
"""
import unittest
from term import Term


class TestTerm(unittest.TestCase):

    def setUp(self):
        self._term = Term(2, 7)

    def test_get_power(self):
        self.assertEqual(self._term.get_power(), 7)

    def test_get_coefficient(self):
        self.assertEqual(self._term.get_coefficient(), 2)

    def tearDown(self):
        self._term = None


if __name__ == '__main__':
    unittest.main()
