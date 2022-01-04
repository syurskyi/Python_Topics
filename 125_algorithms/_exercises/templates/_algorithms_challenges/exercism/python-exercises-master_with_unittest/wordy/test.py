_______ unittest

____ wordy _______ calculate


c_ WordyTest(unittest.TestCase):
    ___ test_simple_add_1
        assertEqual(calculate("What is 5 plus 13?"), 18)

    ___ test_simple_add_2
        assertEqual(calculate("What is 5 plus -13?"), -8)

    ___ test_simple_sub_1
        assertEqual(calculate("What is 103 minus 97?"), 6)

    ___ test_simple_sub_2
        assertEqual(calculate("What is 97 minus 103?"), -6)

    ___ test_simple_mult
        assertEqual(calculate("What is 7 multiplied by 3?"), 21)

    ___ test_simple_div
        assertEqual(calculate("What is 45 divided by 5?"), 9)

    ___ test_add_negative_numbers
        assertEqual(calculate("What is -1 plus -10?"), -11)

    ___ test_add_more_digits
        assertEqual(calculate("What is 123 plus 45678?"), 45801)

    ___ test_add_twice
        assertEqual(calculate("What is 1 plus 2 plus 1?"), 4)

    ___ test_add_then_subtract
        assertEqual(calculate("What is 1 plus 5 minus -8?"), 14)

    ___ test_subtract_twice
        assertEqual(calculate("What is 20 minus 14 minus 13?"), -7)

    ___ test_multiply_twice
        assertEqual(
            calculate("What is 2 multiplied by -2 multiplied by 3?"), -12)

    ___ test_add_then_multiply
        assertEqual(calculate("What is -3 plus 7 multiplied by -2?"), -8)

    ___ test_divide_twice
        assertEqual(
            calculate("What is -12000 divided by 25 divided by -30?"), 16)

    ___ test_invalid_operation
        assertRaises(ValueError, calculate, "What is 4 xor 7?")

    ___ test_missing_operation
        assertRaises(ValueError, calculate, "What is 2 2 minus 3?")

    ___ test_missing_number
        assertRaises(ValueError, calculate,
                          "What is 7 plus multiplied by -2?")

    ___ test_irrelevant_question
        assertRaises(ValueError, calculate, "Which is greater, 3 or 2?")


__ _____ __ _____
    unittest.main()
