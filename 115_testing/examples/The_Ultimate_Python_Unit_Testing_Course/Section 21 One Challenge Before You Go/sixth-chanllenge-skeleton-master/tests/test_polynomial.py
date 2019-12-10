"""
    This is just an example to get you started.
    Here are some ideas on things you should test for:
    1- Test for None values.
    2- Test if the multiply method in the Polynomial class still works even if:
        - the power is zero or lower.
        - the coefficient is zero or lower.
        Note: we need to test the above because we might do some math that cases errors.
    3- Test if the print_poly method prints terms in ascending order.
"""

import unittest
from term import Term
from polynomial import Polynomial


class TestPolynomialMultiplier(unittest.TestCase):

    def setUp(self):
        self._first_polynomial = Polynomial([Term(2, 2), Term(2, 3)])
        self._second_polynomial = Polynomial([Term(2, 4), Term(2, 2)])
        self._result = {6: 4,
                        4: 4,
                        7: 4,
                        5: 4}

    def test_multiply(self):
        self._first_polynomial.multiply(self._second_polynomial)
        for k, v in self._first_polynomial.get_result().items():
            self.assertEqual(self._first_polynomial.get_result().get(k), self._result.get(k))

    def tearDown(self):
        self._term = None


if __name__ == '__main__':
    unittest.main()
