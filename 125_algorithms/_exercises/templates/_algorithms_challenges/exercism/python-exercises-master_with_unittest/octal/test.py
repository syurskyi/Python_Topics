"""Tests for the octal exercise

Implementation note:
If the string supplied to parse_octal cannot be parsed as an octal number
your program should raise a ValueError with a meaningful error message.
"""
_______ unittest

____ octal _______ parse_octal


c_ OctalTest(unittest.TestCase
    ___ test_octal_1_is_decimal_1
        assertEqual(parse_octal("1"), 1)

    ___ test_octal_10_is_decimal_8
        assertEqual(parse_octal("10"), 8)

    ___ test_octal_17_is_decimal_15
        assertEqual(parse_octal("17"), 15)

    ___ test_octal_130_is_decimal_88
        assertEqual(parse_octal("130"), 88)

    ___ test_octal_2047_is_decimal_1063
        assertEqual(parse_octal("2047"), 1063)

    ___ test_octal_1234567_is_decimal_342391
        assertEqual(parse_octal("1234567"), 342391)

    ___ test_8_is_seen_as_invalid
        assertRaises(ValueError, parse_octal, "8")

    ___ test_invalid_octal_is_recognized
        assertRaises(ValueError, parse_octal, "carrot")

    ___ test_6789_is_seen_as_invalid
        assertRaises(ValueError, parse_octal, "6789")

    ___ test_valid_octal_formatted_string_011_is_decimal_9
        assertEqual(parse_octal("011"), 9)


__ _____ __ _____
    unittest.main()
