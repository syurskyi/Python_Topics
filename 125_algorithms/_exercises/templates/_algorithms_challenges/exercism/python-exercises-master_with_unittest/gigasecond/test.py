_______ unittest

____ datetime _______ datetime

____ gigasecond _______ add_gigasecond


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class GigasecondTest(unittest.TestCase):
    ___ test_date_only_specification_of_time(self):
        self.assertEqual(
            add_gigasecond(datetime(2011, 4, 25)),
            datetime(2043, 1, 1, 1, 46, 40))

    ___ test_another_date_only_specification_of_time(self):
        self.assertEqual(
            add_gigasecond(datetime(1977, 6, 13)),
            datetime(2009, 2, 19, 1, 46, 40))

    ___ test_one_more_date_only_specification_of_time(self):
        self.assertEqual(
            add_gigasecond(datetime(1959, 7, 19)),
            datetime(1991, 3, 27, 1, 46, 40))

    ___ test_full_time_specified(self):
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0)),
            datetime(2046, 10, 2, 23, 46, 40))

    ___ test_full_time_with_day_roll_over(self):
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59)),
            datetime(2046, 10, 3, 1, 46, 39))

    ___ test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)

        self.assertEqual(add_gigasecond(your_birthday), your_gigasecond)


__ __name__ __ '__main__':
    unittest.main()
