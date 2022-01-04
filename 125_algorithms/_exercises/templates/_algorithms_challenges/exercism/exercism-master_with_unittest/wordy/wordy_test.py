_______ unittest

____ wordy _______ calculate


c_ WordyTest(unittest.TestCase):

    ___ test_simple_add_1
        assertEqual(18, calculate("What is 5 plus 13?"))

    ___ test_simple_add_2
        assertEqual(-8, calculate("What is 5 plus -13?"))

    ___ test_simple_sub_1
        assertEqual(6, calculate("What is 103 minus 97?"))

    ___ test_simple_sub_2
        assertEqual(-6, calculate("What is 97 minus 103?"))

    ___ test_simple_mult
        assertEqual(21, calculate("What is 7 multiplied by 3?"))

    ___ test_simple_div
        assertEqual(9, calculate("What is 45 divided by 5?"))

    ___ test_add_negative_numbers
        assertEqual(-11, calculate("What is -1 plus -10?"))

    ___ test_add_more_digits
        assertEqual(45801, calculate("What is 123 plus 45678?"))

    ___ test_add_twice
        assertEqual(4, calculate("What is 1 plus 2 plus 1?"))

    ___ test_add_then_subtract
        assertEqual(14, calculate("What is 1 plus 5 minus -8?"))

    ___ test_subtract_twice
        assertEqual(-7, calculate("What is 20 minus 14 minus 13?"))

    ___ test_multiply_twice
        assertEqual(-12, calculate("What is 2 multiplied by -2 "
                                        "multiplied by 3?"))

    ___ test_add_then_multiply
        assertEqual(-8, calculate("What is -3 plus 7 multiplied by -2?"))

    ___ test_divide_twice
        assertEqual(
            16, calculate("What is -12000 divided by 25 divided by -30?"))

    ___ test_invalid_operation
        assertRaises(ValueError, calculate, "What is 4 xor 7?")

    ___ test_missing_operation
        assertRaises(ValueError, calculate, "What is 2 2 minus 3?")

    ___ test_missing_number
        assertRaises(ValueError, calculate, "What is 7 plus "
                                                 "multiplied by -2?")

    ___ test_irrelevant_question
        assertRaises(ValueError, calculate, "Which is greater, 3 or 2?")


__ _____ __ _____
    unittest.main()
