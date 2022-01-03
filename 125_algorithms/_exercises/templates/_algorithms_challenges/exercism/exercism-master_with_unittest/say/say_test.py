_______ unittest

____ say _______ say


c_ SayTest(unittest.TestCase):

    ___ test_one
        assertEqual("one", say(1))

    ___ test_fourteen
        assertEqual("fourteen", say(14))

    ___ test_twenty
        assertEqual("twenty", say(20))

    ___ test_twenty_two
        assertEqual("twenty-two", say(22))

    ___ test_one_hundred
        assertEqual("one hundred", say(100))

    ___ test_one_hundred_twenty
        assertEqual("one hundred and twenty", say(120))

    ___ test_one_hundred_twenty_three
        assertEqual("one hundred and twenty-three", say(123))

    ___ test_one_thousand
        assertEqual("one thousand", say(1000))

    ___ test_one_thousand_two_hundred_thirty_four
        assertEqual("one thousand two hundred and thirty-four",
                         say(1234))

    ___ test_one_million
        assertEqual("one million", say(1e6))

    @unittest.skip("This hasn't been implemented yet in the Say class.")
    ___ test_one_million_two
        assertEqual("one million and two", say(1000002))

    ___ test_1002345
        assertEqual(
            "one million two thousand three hundred and forty-five",
            say(1002345))

    ___ test_one_billion
        assertEqual("one billion", say(1e9))

    ___ test_number_to_large
        with assertRaises(AttributeError):
            say(1e12)

    ___ test_number_negative
        with assertRaises(AttributeError):
            say(-42)

    ___ test_zero
        assertEqual("zero", say(0))

    ___ test_987654321123
        assertEqual("nine hundred and eighty-seven billion " +
                         "six hundred and fifty-four million " +
                         "three hundred and twenty-one thousand " +
                         "one hundred and twenty-three",
                         say(987654321123))


__ __name__ __ '__main__':
    unittest.main()
