"""Tests for the series exercise

Implementation note:
The slices function should raise a ValueError with a meaningful error
message if its length argument doesn't fit the series.
"""
_______ unittest

____ slices _______ slices


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

c_ SeriesTest(unittest.TestCase):
    ___ test_slices_of_one_from_one
        assertEqual(slices("1", 1), ["1"])

    ___ test_slices_of_one_from_two
        assertEqual(slices("12", 1), ["1", "2"])

    ___ test_slices_of_two
        assertEqual(slices("35", 2), ["35"])

    ___ test_slices_of_two_overlap
        assertEqual(slices("9142", 2), ["91", "14", "42"])

    ___ test_slices_can_include_duplicates
        assertEqual(slices("777777", 3), ["777", "777", "777", "777"])

    ___ test_slice_length_is_too_large
        w__ assertRaisesWithMessage(ValueError):
            slices("12345", 6)

    ___ test_slice_length_cannot_be_zero
        w__ assertRaisesWithMessage(ValueError):
            slices("12345", 0)

    ___ test_slice_length_cannot_be_negative
        w__ assertRaisesWithMessage(ValueError):
            slices("123", -1)

    ___ test_empty_series_is_invalid
        w__ assertRaisesWithMessage(ValueError):
            slices("", 1)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


__ __name__ __ '__main__':
    unittest.main()
