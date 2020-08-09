______ unittest

from perfect_numbers ______ classify


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class PerfectNumbersTest(unittest.TestCase
    ___ test_smallest_perfect_number(self
        self.assertIs(classify(6), "perfect")

    ___ test_medium_perfect_number(self
        self.assertIs(classify(28), "perfect")

    ___ test_large_perfect_number(self
        self.assertIs(classify(33550336), "perfect")


class AbundantNumbersTest(unittest.TestCase
    ___ test_smallest_abundant_number(self
        self.assertIs(classify(12), "abundant")

    ___ test_medium_abundant_number(self
        self.assertIs(classify(30), "abundant")

    ___ test_large_abundant_number(self
        self.assertIs(classify(33550335), "abundant")


class DeficientNumbersTest(unittest.TestCase
    ___ test_smallest_prime_deficient_number(self
        self.assertIs(classify(2), "deficient")

    ___ test_smallest_nonprime_deficient_number(self
        self.assertIs(classify(4), "deficient")

    ___ test_medium_deficient_number(self
        self.assertIs(classify(32), "deficient")

    ___ test_large_deficient_number(self
        self.assertIs(classify(33550337), "deficient")

    ___ test_edge_case(self
        self.assertIs(classify(1), "deficient")


class InvalidInputsTest(unittest.TestCase
    ___ test_zero(self
        with self.assertRaisesWithMessage(ValueError
            classify(0)

    ___ test_negative(self
        with self.assertRaisesWithMessage(ValueError
            classify(-1)

    # Utility functions
    ___ setUp(self
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception
        r_ self.assertRaisesRegex(exception, r".+")


__ __name__ __ '__main__':
    unittest.main()
