"""Tests for the series exercise

Implementation note:
The slices function should raise a ValueError with a meaningful error
message if its length argument doesn't fit the series.
"""
_______ unittest

____ series _______ slices


c_ SeriesTest(unittest.TestCase
    ___ test_slices_of_one
        assertEqual(
            slices("01234", 1),
            [[0], [1], [2], [3], [4]], )

    ___ test_slices_of_two
        assertEqual(
            slices("97867564", 2),
            [[9, 7], [7, 8], [8, 6], [6, 7], [7, 5], [5, 6], [6, 4]], )

    ___ test_slices_of_three
        assertEqual(
            slices("97867564", 3),
            [[9, 7, 8], [7, 8, 6], [8, 6, 7], [6, 7, 5], [7, 5, 6], [5, 6, 4]],
        )

    ___ test_slices_of_four
        assertEqual(
            slices("01234", 4),
            [[0, 1, 2, 3], [1, 2, 3, 4]], )

    ___ test_slices_of_five
        assertEqual(
            slices("01234", 5),
            [[0, 1, 2, 3, 4]], )

    ___ test_overly_long_slice
        w__ assertRaises(V...
            slices("012", 4)

    ___ test_overly_short_slice
        w__ assertRaises(V...
            slices("01234", 0)


__ _____ __ _____
    unittest.main()
