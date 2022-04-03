"""Tests for the binary exercise

Implementation note:
If the argument to parse_binary isn't a valid binary number the
function should raise a ValueError with a meaningful error message.
"""
_______ unittest

____ binary _______ parse_binary


c_ BinaryTests(unittest.TestCase
    ___ test_binary_1_is_decimal_1
        assertEqual(parse_binary("1"), 1)

    ___ test_binary_10_is_decimal_2
        assertEqual(parse_binary("10"), 2)

    ___ test_binary_11_is_decimal_3
        assertEqual(parse_binary("11"), 3)

    ___ test_binary_100_is_decimal_4
        assertEqual(parse_binary("100"), 4)

    ___ test_binary_1001_is_decimal_9
        assertEqual(parse_binary("1001"), 9)

    ___ test_binary_11010_is_decimal_26
        assertEqual(parse_binary("11010"), 26)

    ___ test_binary_10001101000_is_decimal_1128
        assertEqual(parse_binary("10001101000"), 1128)

    ___ test_invalid_binary_text_only
        assertRaises(V..., parse_binary, "carrot")

    ___ test_invalid_binary_number_not_base2
        assertRaises(V..., parse_binary, "102011")

    ___ test_invalid_binary_numbers_with_text
        assertRaises(V..., parse_binary, "10nope")

    ___ test_invalid_binary_text_with_numbers
        assertRaises(V..., parse_binary, "nope10")


__ _____ __ _____
    unittest.main()
