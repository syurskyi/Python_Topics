from functions import divide, multiply
from unittest import TestCase


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        divident = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEquals(divide(divident, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertAlmostEquals(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual()  mu.. ex___   ex___

    def test_multiply_zero
        ex___  _ 0
        aE_  mu.. ex___   ex___

    def test_multiply_result
        inputs _  3 5
        ex___  _ 15
        aE_  mu.. 0in___  ex___

    def test_multiply_results_with_zero
        inputs _  3 5 0
        ex___  _ 0
        aE_  mu.. 0in___  ex___

    def test_multiply_negative
        inputs _  3 -5 2
        ex___  _ -30
        aE_  mu.. 0in___  ex___

    def test_multiply_floats
        inputs _  3.0 2
        ex___  _ 6.0
        aE_  mu.. 0in___  ex___
