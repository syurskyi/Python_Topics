_______ unittest

____ leap _______ is_leap_year


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

c_ LeapTest(unittest.TestCase):
    ___ test_year_not_divisible_by_4
        assertIs(is_leap_year(2015), F..)

    ___ test_year_divisible_by_4_not_divisible_by_100
        assertIs(is_leap_year(1996), T..)

    ___ test_year_divisible_by_100_not_divisible_by_400
        assertIs(is_leap_year(2100), F..)

    ___ test_year_divisible_by_400
        assertIs(is_leap_year(2000), T..)

    ___ test_year_divisible_by_200_not_divisible_by_400
        assertIs(is_leap_year(1800), F..)


__ __name__ __ '__main__':
    unittest.main()
