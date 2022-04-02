_______ unittest

____ d__ _______ d__

____ gigasecond _______ add_gigasecond


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ GigasecondTest(unittest.TestCase
    ___ test_date_only_specification_of_time
        assertEqual(
            add_gigasecond(d__(2011, 4, 25)),
            d__(2043, 1, 1, 1, 46, 40))

    ___ test_another_date_only_specification_of_time
        assertEqual(
            add_gigasecond(d__(1977, 6, 13)),
            d__(2009, 2, 19, 1, 46, 40))

    ___ test_one_more_date_only_specification_of_time
        assertEqual(
            add_gigasecond(d__(1959, 7, 19)),
            d__(1991, 3, 27, 1, 46, 40))

    ___ test_full_time_specified
        assertEqual(
            add_gigasecond(d__(2015, 1, 24, 22, 0, 0)),
            d__(2046, 10, 2, 23, 46, 40))

    ___ test_full_time_with_day_roll_over
        assertEqual(
            add_gigasecond(d__(2015, 1, 24, 23, 59, 59)),
            d__(2046, 10, 3, 1, 46, 39))

    ___ test_yourself
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = d__(1970, 1, 1)
        your_gigasecond = d__(2001, 9, 9, 1, 46, 40)

        assertEqual(add_gigasecond(your_birthday), your_gigasecond)


__ _____ __ _____
    unittest.main()
