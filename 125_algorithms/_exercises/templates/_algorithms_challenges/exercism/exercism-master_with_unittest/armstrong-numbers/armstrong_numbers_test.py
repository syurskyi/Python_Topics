import unittest

from armstrong_numbers import is_armstrong


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class ArmstrongNumbersTest(unittest.TestCase):

    ___ test_single_digit_numbers_are_armstrong_numbers(self):
        self.assertIs(is_armstrong(5), True)

    ___ test_there_are_no_two_digit_armstrong_numbers(self):
        self.assertIs(is_armstrong(10), False)

    ___ test_three_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong(153), True)

    ___ test_three_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong(100), False)

    ___ test_four_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong(9474), True)

    ___ test_four_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong(9475), False)

    ___ test_seven_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong(9926315), True)

    ___ test_seven_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong(9926314), False)


__ __name__ == '__main__':
    unittest.main()
