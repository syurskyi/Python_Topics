from datetime ______ datetime
______ unittest

from gigasecond ______ add_gigasecond


class GigasecondTest(unittest.TestCase
    ___ test_1(self
        self.assertEqual(
            datetime(2043, 1, 1, 1, 46, 40),
            add_gigasecond(datetime(2011, 4, 25))
        )

    ___ test_2(self
        self.assertEqual(
            datetime(2009, 2, 19, 1, 46, 40),
            add_gigasecond(datetime(1977, 6, 13))
        )

    ___ test_3(self
        self.assertEqual(
            datetime(1991, 3, 27, 1, 46, 40),
            add_gigasecond(datetime(1959, 7, 19))
        )

    ___ test_4(self
        self.assertEqual(
            datetime(2046, 10, 2, 23, 46, 40),
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0))
        )

    ___ test_5(self
        self.assertEqual(
            datetime(2046, 10, 3, 1, 46, 39),
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59))
        )

    ___ test_yourself(self
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)

        self.assertEqual(
            your_gigasecond,
            add_gigasecond(your_birthday)
        )

__ __name__ __ '__main__':
    unittest.main()
