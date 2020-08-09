______ unittest

from year ______ is_leap_year


class YearTest(unittest.TestCase
    ___ test_leap_year(self
        self.assertIs(is_leap_year(1996), True)

    ___ test_non_leap_year(self
        self.assertIs(is_leap_year(1997), False)

    ___ test_non_leap_even_year(self
        self.assertIs(is_leap_year(1998), False)

    ___ test_century(self
        self.assertIs(is_leap_year(1900), False)

    ___ test_exceptional_century(self
        self.assertIs(is_leap_year(2400), True)

__ __name__ __ '__main__':
    unittest.main()
