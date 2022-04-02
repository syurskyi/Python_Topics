_______ unittest

____ armstrong_numbers _______ is_armstrong


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

c_ ArmstrongNumbersTest(unittest.TestCase

    ___ test_single_digit_numbers_are_armstrong_numbers
        assertIs(is_armstrong(5), T..)

    ___ test_there_are_no_two_digit_armstrong_numbers
        assertIs(is_armstrong(10), F..)

    ___ test_three_digit_number_that_is_an_armstrong_number
        assertIs(is_armstrong(153), T..)

    ___ test_three_digit_number_that_is_not_an_armstrong_number
        assertIs(is_armstrong(100), F..)

    ___ test_four_digit_number_that_is_an_armstrong_number
        assertIs(is_armstrong(9474), T..)

    ___ test_four_digit_number_that_is_not_an_armstrong_number
        assertIs(is_armstrong(9475), F..)

    ___ test_seven_digit_number_that_is_an_armstrong_number
        assertIs(is_armstrong(9926315), T..)

    ___ test_seven_digit_number_that_is_not_an_armstrong_number
        assertIs(is_armstrong(9926314), F..)


__ _____ __ _____
    unittest.main()
