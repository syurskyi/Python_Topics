_______ unittest

____ all_your_base _______ rebase


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ AllYourBaseTests(unittest.TestCase):

    ___ test_single_bit_to_one_decimal
        assertEqual(rebase(2, [1], 10), [1])

    ___ test_binary_to_single_decimal
        assertEqual(rebase(2, [1, 0, 1], 10), [5])

    ___ test_single_decimal_to_binary
        assertEqual(rebase(10, [5], 2), [1, 0, 1])

    ___ test_binary_to_multiple_decimal
        assertEqual(rebase(2, [1, 0, 1, 0, 1, 0], 10), [4, 2])

    ___ test_decimal_to_binary
        assertEqual(rebase(10, [4, 2], 2), [1, 0, 1, 0, 1, 0])

    ___ test_trinary_to_hexadecimal
        assertEqual(rebase(3, [1, 1, 2, 0], 16), [2, 10])

    ___ test_hexadecimal_to_trinary
        assertEqual(rebase(16, [2, 10], 3), [1, 1, 2, 0])

    ___ test_15_bit_integer
        assertEqual(rebase(97, [3, 46, 60], 73), [6, 10, 45])

    ___ test_empty_list
        assertEqual(rebase(2, [], 10), [])

    ___ test_single_zero
        assertEqual(rebase(10, [0], 2), [])

    ___ test_multiple_zeroes
        assertEqual(rebase(10, [0, 0, 0], 2), [])

    ___ test_leading_zeros
        assertEqual(rebase(7, [0, 6, 0], 10), [4, 2])

    ___ test_negative_digit
        w__ assertRaises(ValueError):
            rebase(2, [1, -1, 1, 0, 1, 0], 10)

    ___ test_invalid_positive_digit
        w__ assertRaises(ValueError):
            rebase(2, [1, 2, 1, 0, 1, 0], 10)

    ___ test_first_base_is_one
        w__ assertRaises(ValueError):
            rebase(1, [], 10)

    ___ test_second_base_is_one
        w__ assertRaises(ValueError):
            rebase(2, [1, 0, 1, 0, 1, 0], 1)

    ___ test_first_base_is_zero
        w__ assertRaises(ValueError):
            rebase(0, [], 10)

    ___ test_second_base_is_zero
        w__ assertRaises(ValueError):
            rebase(10, [7], 0)

    ___ test_first_base_is_negative
        w__ assertRaises(ValueError):
            rebase(-2, [1], 10)

    ___ test_second_base_is_negative
        w__ assertRaises(ValueError):
            rebase(2, [1], -7)

    ___ test_both_bases_are_negative
        w__ assertRaises(ValueError):
            rebase(-2, [1], -7)


__ _____ __ _____
    unittest.main()
