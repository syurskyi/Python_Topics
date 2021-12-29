_______ unittest

____ say _______ say


class SayTest(unittest.TestCase):

    ___ test_one(self):
        self.assertEqual("one", say(1))

    ___ test_fourteen(self):
        self.assertEqual("fourteen", say(14))

    ___ test_twenty(self):
        self.assertEqual("twenty", say(20))

    ___ test_twenty_two(self):
        self.assertEqual("twenty-two", say(22))

    ___ test_one_hundred(self):
        self.assertEqual("one hundred", say(100))

    ___ test_one_hundred_twenty(self):
        self.assertEqual("one hundred and twenty", say(120))

    ___ test_one_hundred_twenty_three(self):
        self.assertEqual("one hundred and twenty-three", say(123))

    ___ test_one_thousand(self):
        self.assertEqual("one thousand", say(1000))

    ___ test_one_thousand_two_hundred_thirty_four(self):
        self.assertEqual("one thousand two hundred and thirty-four",
                         say(1234))

    ___ test_one_million(self):
        self.assertEqual("one million", say(1e6))

    @unittest.skip("This hasn't been implemented yet in the Say class.")
    ___ test_one_million_two(self):
        self.assertEqual("one million and two", say(1000002))

    ___ test_1002345(self):
        self.assertEqual(
            "one million two thousand three hundred and forty-five",
            say(1002345))

    ___ test_one_billion(self):
        self.assertEqual("one billion", say(1e9))

    ___ test_number_to_large(self):
        with self.assertRaises(AttributeError):
            say(1e12)

    ___ test_number_negative(self):
        with self.assertRaises(AttributeError):
            say(-42)

    ___ test_zero(self):
        self.assertEqual("zero", say(0))

    ___ test_987654321123(self):
        self.assertEqual("nine hundred and eighty-seven billion " +
                         "six hundred and fifty-four million " +
                         "three hundred and twenty-one thousand " +
                         "one hundred and twenty-three",
                         say(987654321123))


__ __name__ __ '__main__':
    unittest.main()
