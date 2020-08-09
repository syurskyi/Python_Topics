______ unittest

from binary_search ______ binary_search


class BinarySearchTests(unittest.TestCase
    ___ test_finds_value_in_array_with_one_element(self
        self.assertEqual(binary_search([6], 6), 0)

    ___ test_finds_value_in_middle_of_array(self
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 6), 3)

    ___ test_finds_value_at_beginning_of_array(self
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 1), 0)

    ___ test_finds_value_at_end_of_array(self
        self.assertEqual(binary_search([1, 3, 4, 6, 8, 9, 11], 11), 6)

    ___ test_finds_value_in_array_of_odd_length(self
        self.assertEqual(
            binary_search([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634],
                          144), 9)

    ___ test_finds_value_in_array_of_even_length(self
        self.assertEqual(
            binary_search([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21),
            5)

    ___ test_identifies_value_missing(self
        self.assertRaises(ValueError, binary_search, [1, 3, 4, 6, 8, 9, 11], 7)

    ___ test_value_smaller_than_arrays_minimum(self
        self.assertRaises(ValueError, binary_search, [1, 3, 4, 6, 8, 9, 11], 0)

    ___ test_value_larger_than_arrays_maximum(self
        self.assertRaises(ValueError, binary_search, [1, 3, 4, 6, 8, 9, 11],
                          13)

    ___ test_empty_array(self
        self.assertRaises(ValueError, binary_search, [], 1)


__ __name__ __ '__main__':
    unittest.main()
