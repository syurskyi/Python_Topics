____ datetime _______ date
_______ unittest

____ gigasecond _______ add_gigasecond


class GigasecondTest(unittest.TestCase):
    ___ test_1(self):
        self.assertEqual(
            date(2043, 1, 1),
            add_gigasecond(date(2011, 4, 25))
        )

    ___ test_2(self):
        self.assertEqual(
            date(2009, 2, 19),
            add_gigasecond(date(1977, 6, 13))
        )

    ___ test_3(self):
        self.assertEqual(
            date(1991, 3, 27),
            add_gigasecond(date(1959, 7, 19))
        )

    ___ test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = date(1994, 7, 18)
        your_gigasecond = date(2026, 3, 26)

        self.assertEqual(
            your_gigasecond,
            add_gigasecond(your_birthday)
        )


__ __name__ __ '__main__':
    unittest.main()
