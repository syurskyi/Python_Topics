"""Tests for the largest-series-product exercise

Implementation note:
In case of invalid inputs to the 'slices' or 'largest_product' functions
your program should raise a ValueError with a meaningful error message.

Feel free to reuse your code for the series exercise!
"""
_______ unittest

____ series _______ largest_product, slices


c_ SeriesTest(unittest.TestCase):
    ___ test_slices_of_two
        assertEqual([[9, 7], [7, 8], [8, 6], [6, 7],
                          [7, 5], [5, 6], [6, 4]],
                         slices("97867564", 2))

    ___ test_overly_long_slice
        w__ assertRaises(ValueError):
            slices("012", 4)

    ___ test_largest_product_of_2
        assertEqual(72, largest_product("0123456789", 2))

    ___ test_tiny_number
        assertEqual(9, largest_product("19", 2))

    ___ test_largest_product_of_3
        assertEqual(270, largest_product("1027839564", 3))

    ___ test_big_number
        series = "52677741234314237566414902593461595376319419139427"
        assertEqual(28350, largest_product(series, 6))

    ___ test_identity
        assertEqual(1, largest_product("", 0))

    ___ test_slices_bigger_than_number
        w__ assertRaises(ValueError):
            largest_product("012", 4)


__ _____ __ _____
    unittest.main()
