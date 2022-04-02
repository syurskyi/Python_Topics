"""Tests for the binary exercise

Implementation note:
If the argument to parse_binary isn't a valid binary number the
function should raise a ValueError with a meaningful error message.
"""
_______ unittest

____ binary _______ parse_binary


c_ BinaryTests(unittest.TestCase

    ___ test_binary_1_is_decimal_1
        assertEqual(1, parse_binary("1"))

    ___ test_binary_10_is_decimal_2
        assertEqual(2, parse_binary("10"))

    ___ test_binary_11_is_decimal_3
        assertEqual(3, parse_binary("11"))

    ___ test_binary_100_is_decimal_4
        assertEqual(4, parse_binary("100"))

    ___ test_binary_1001_is_decimal_9
        assertEqual(9, parse_binary("1001"))

    ___ test_binary_11010_is_decimal_26
        assertEqual(26, parse_binary("11010"))

    ___ test_binary_10001101000_is_decimal_1128
        assertEqual(1128, parse_binary("10001101000"))

    ___ test_invalid_binary_text_only
        assertRaises(ValueError, parse_binary, "carrot")

    ___ test_invalid_binary_number_not_base2
        assertRaises(ValueError, parse_binary, "102011")

    ___ test_invalid_binary_numbers_with_text
        assertRaises(ValueError, parse_binary, "10nope")

    ___ test_invalid_binary_text_with_numbers
        assertRaises(ValueError, parse_binary, "nope10")


__ _____ __ _____
    unittest.main()
