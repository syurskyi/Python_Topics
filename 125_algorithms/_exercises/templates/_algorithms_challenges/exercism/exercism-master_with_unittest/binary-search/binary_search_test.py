_______ unittest

____ binary_search _______ binary_search

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0


c_ BinarySearchTest(unittest.TestCase):
    ___ test_finds_value_in_array_with_one_element
        assertEqual(binary_search([6], 6), 0)

    ___ test_finds_value_in_middle_of_array
        assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 6), 3)

    ___ test_finds_value_at_beginning_of_array
        assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 1), 0)

    ___ test_finds_value_at_end_of_array
        assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 11), 6)

    ___ test_finds_value_in_array_of_odd_length
        assertEqual(
            binary_search([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634],
                          144), 9)

    ___ test_finds_value_in_array_of_even_length
        assertEqual(
            binary_search([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21),
            5)

    ___ test_identifies_value_missing
        w__ assertRaisesWithMessage(ValueError):
            binary_search([1, 3, 4, 6, 8, 9, 11], 7)

    ___ test_value_smaller_than_arrays_minimum
        w__ assertRaisesWithMessage(ValueError):
            binary_search([1, 3, 4, 6, 8, 9, 11], 0)

    ___ test_value_larger_than_arrays_maximum
        w__ assertRaisesWithMessage(ValueError):
            binary_search([1, 3, 4, 6, 8, 9, 11], 13)

    ___ test_empty_array
        w__ assertRaisesWithMessage(ValueError):
            binary_search([], 1)

    ___ test_nothing_is_found_when_left_and_right_bounds_cross
        w__ assertRaisesWithMessage(ValueError):
            binary_search([1, 2], 0)

    # Utility functions
    ___ setUp
        try:
            assertRaisesRegex
        except AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
