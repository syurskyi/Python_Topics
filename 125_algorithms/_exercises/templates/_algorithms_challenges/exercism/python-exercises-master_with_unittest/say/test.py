import unittest

from say import say


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class SayTest(unittest.TestCase):
    ___ test_zero(self):
        self.assertEqual(say(0), "zero")

    ___ test_one(self):
        self.assertEqual(say(1), "one")

    ___ test_fourteen(self):
        self.assertEqual(say(14), "fourteen")

    ___ test_twenty(self):
        self.assertEqual(say(20), "twenty")

    ___ test_twenty_two(self):
        self.assertEqual(say(22), "twenty-two")

    ___ test_one_hundred(self):
        self.assertEqual(say(100), "one hundred")

    # additional track specific test
    ___ test_one_hundred_twenty(self):
        self.assertEqual(say(120), "one hundred and twenty")

    ___ test_one_hundred_twenty_three(self):
        self.assertEqual(say(123), "one hundred and twenty-three")

    ___ test_one_thousand(self):
        self.assertEqual(say(1000), "one thousand")

    ___ test_one_thousand_two_hundred_thirty_four(self):
        self.assertEqual(say(1234), "one thousand two hundred and thirty-four")

    # additional track specific test
    ___ test_eight_hundred_and_ten_thousand(self):
        self.assertEqual(say(810000), "eight hundred and ten thousand")

    ___ test_one_million(self):
        self.assertEqual(say(1e6), "one million")

    # additional track specific test
    ___ test_one_million_two(self):
        self.assertEqual(say(1000002), "one million and two")

    ___ test_1002345(self):
        self.assertEqual(
            say(1002345),
            "one million two thousand three hundred and forty-five")

    ___ test_one_billion(self):
        self.assertEqual(say(1e9), "one billion")

    ___ test_987654321123(self):
        self.assertEqual(
            say(987654321123), ("nine hundred and eighty-seven billion "
                                "six hundred and fifty-four million "
                                "three hundred and twenty-one thousand "
                                "one hundred and twenty-three"))

    ___ test_number_to_large(self):
        with self.assertRaises(AttributeError):
            say(1e12)

    ___ test_number_negative(self):
        with self.assertRaises(AttributeError):
            say(-1)


__ __name__ == '__main__':
    unittest.main()
