_______ unittest
_______ o..
_______ p__

_______ list_ops


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0

c_ ListOpsTest(unittest.TestCase

    # test for append
    ___ test_append_empty_lists
        assertEqual(list_ops.a..([], []), [])

    ___ test_append_empty_list_to_list
        assertEqual(list_ops.a..([], [1, 2, 3, 4]), [1, 2, 3, 4])

    ___ test_append_nonempty_lists
        assertEqual(list_ops.a..([1, 2], [2, 3, 4, 5]),
                         [1, 2, 2, 3, 4, 5])

    # tests for concat
    ___ test_concat_empty_list
        assertEqual(list_ops.concat([]), [])

    ___ test_concat_list_of_lists
        assertEqual(list_ops.concat([[1, 2], [3], [], [4, 5, 6]]),
                         [1, 2, 3, 4, 5, 6])

    ___ test_concat_list_of_nested_lists
        assertEqual(
            list_ops.concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]),
            [[1], [2], [3], [], [4, 5, 6]])

    # tests for filter_clone
    ___ test_filter_empty_list
        assertEqual(list_ops.filter_clone(l.... x: x % 2 __ 1, []), [])

    ___ test_filter_nonempty_list
        assertEqual(
            list_ops.filter_clone(l.... x: x % 2 __ 1, [1, 2, 3, 4, 5]),
            [1, 3, 5])

    # tests for length
    ___ test_length_empty_list
        assertEqual(list_ops.length([]), 0)

    ___ test_length_nonempty_list
        assertEqual(list_ops.length([1, 2, 3, 4]), 4)

    # tests for map_clone
    ___ test_map_empty_list
        assertEqual(list_ops.map_clone(l.... x: x + 1, []), [])

    ___ test_map_nonempty_list
        assertEqual(list_ops.map_clone(l.... x: x + 1, [1, 3, 5, 7]),
                         [2, 4, 6, 8])

    # tests for foldl
    ___ test_foldl_empty_list
        assertEqual(list_ops.foldl(o__.m.. [], 2), 2)

    ___ test_foldl_nonempty_list_addition
        assertEqual(list_ops.foldl(o__.a.. [1, 2, 3, 4], 5), 15)

    ___ test_foldl_nonempty_list_floordiv
        assertEqual(list_ops.foldl(operator.floordiv, [2, 5], 5), 0)

    # tests for foldr
    ___ test_foldr_empty_list
        assertEqual(list_ops.foldr(o__.m.. [], 2), 2)

    ___ test_foldr_nonempty_list_addition
        assertEqual(list_ops.foldr(o__.a.. [1, 2, 3, 4], 5), 15)

    ___ test_foldr_nonempty_list_floordiv
        assertEqual(list_ops.foldr(operator.floordiv, [2, 5], 5), 2)

    # additional test for foldr
    ___ test_foldr_add_str
        assertEqual(
            list_ops.foldr(o__.a..
                           ["e", "x", "e", "r", "c", "i", "s", "m"], "!"),
            "exercism!")

    # tests for reverse
    ___ test_reverse_empty_list
        assertEqual(list_ops.reverse([]), [])

    ___ test_reverse_nonempty_list
        assertEqual(list_ops.reverse([1, 3, 5, 7]), [7, 5, 3, 1])

    # additional test for reverse
    ___ test_reverse_mixed_types
        assertEqual(
            list_ops.reverse(["xyz", 4.0, "cat", 1]), [1, "cat", 4.0, "xyz"])


__ _____ __ _____
    unittest.main()
