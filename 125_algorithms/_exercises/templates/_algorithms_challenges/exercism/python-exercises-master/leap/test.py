______ unittest

from leap ______ is_leap_year


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class YearTest(unittest.TestCase
    ___ test_year_not_divisible_by_4(self
        self.assertFalse(is_leap_year(2015))

    ___ test_year_divisible_by_4_not_divisible_by_100(self
        self.assertTrue(is_leap_year(2016))

    ___ test_year_divisible_by_100_not_divisible_by_400(self
        self.assertFalse(is_leap_year(2100))

    ___ test_year_divisible_by_400(self
        self.assertTrue(is_leap_year(2000))


__ __name__ __ '__main__':
    unittest.main()
