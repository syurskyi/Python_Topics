______ unittest

from flatten_array ______ flatten


class FlattenArrayTests(unittest.TestCase

    ___ test_no_nesting(self
        self.assertEqual(flatten([0, 1, 2]), [0, 1, 2])

    ___ test_one_level_nesting(self
        self.assertEqual(flatten([0, [1], 2]), [0, 1, 2])

    ___ test_two_level_nesting(self
        self.assertEqual(flatten([0, [1, [2, 3]], [4]]), [0, 1, 2, 3, 4])

    ___ test_empty_nested_lists(self
        self.assertEqual(flatten([[()]]), [])

    ___ test_with_none_values(self
        inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
        expected = [0, 2, 2, 3, 8, 100, -2]
        self.assertEqual(flatten(inputs), expected)

    ___ test_six_level_nesting(self
        inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(inputs), expected)

    ___ test_all_values_are_none(self
        inputs = [None, [[[None]]], None, None, [[None, None], None], None]
        expected = []
        self.assertEqual(flatten(inputs), expected)

    ___ test_strings(self
        self.assertEqual(flatten(['0', ['1', '2']]), ['0', '1', '2'])


__ __name__ __ '__main__':
    unittest.main()
