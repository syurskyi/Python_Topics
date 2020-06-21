from functions import divide
from unittest import TestCase


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divider = 3
        expected_result = 5.0
        self.assertAlmostEquals(divide(dividend, divider),  expected_result, delta = 0.0001)

    def test_divide_negative(self):
        dividend = 15
        divider = -3
        expected_result = -5.0
        self.assertAlmostEquals(divide(dividend, divider), expected_result, delta = 0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divider = 5
        expected_result = 0
        self.assertAlmostEquals(divide(dividend, divider), expected_result)
