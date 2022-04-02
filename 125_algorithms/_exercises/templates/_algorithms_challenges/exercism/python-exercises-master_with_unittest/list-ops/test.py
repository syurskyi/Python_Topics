_______ unittest
_______ operator

_______ list_ops


c_ ListOpsTest(unittest.TestCase

    # tests for map
    ___ test_map_square
        assertEqual(
            list_ops.map_clone(l.... x: x**2,
                               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    ___ test_map_cube
        assertEqual(
            list_ops.map_clone(l.... x: x**3,
                               [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]),
            [-1, 8, -27, 64, -125, 216, -343, 512, -729, 1000])

    ___ test_map_absolute
        assertEqual(
            list_ops.map_clone(l.... x: abs(x),
                               [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    ___ test_map_empty
        assertEqual(list_ops.map_clone(operator.index, []), [])

    # tests for length
    ___ test_pos_leng
        assertEqual(
            list_ops.length([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]), 10)

    ___ test_empty_len
        assertEqual(list_ops.length([]), 0)

    # tests for filter
    ___ test_filter_odd
        assertEqual(
            list_ops.filter_clone(l.... x: x % 2 != 0, [1, 2, 3, 4, 5, 6]),
            [1, 3, 5])

    ___ test_filter_even
        assertEqual(
            list_ops.filter_clone(l.... x: x % 2 __ 0, [1, 2, 3, 4, 5, 6]),
            [2, 4, 6])

    # tests for reverse
    ___ test_reverse_small
        assertEqual(list_ops.reverse([3, 2, 1]), [1, 2, 3])

    ___ test_reverse_mixed_types
        assertEqual(
            list_ops.reverse(["xyz", 4.0, "cat", 1]), [1, "cat", 4.0, "xyz"])

    ___ test_reverse_empty
        assertEqual(list_ops.reverse([]), [])

    # tests for append
    ___ test_append_tuple
        assertEqual(
            list_ops.a..(["10", "python"], "hello"),
            ["10", "python", "hello"])

    ___ test_append_range
        assertEqual(
            list_ops.a..([100], r..(1000)), [100, r..(1000)])

    ___ test_append_to_empty
        assertEqual(list_ops.a..([], 42), [42])

    # tests for foldl
    ___ test_foldl_sum
        assertEqual(
            list_ops.foldl(operator.add, [1, 2, 3, 4, 5, 6], 0), 21)

    ___ test_foldl_product
        assertEqual(
            list_ops.foldl(operator.mul, [1, 2, 3, 4, 5, 6], 1), 720)

    ___ test_foldl_div
        assertEqual(
            list_ops.foldl(operator.floordiv, [1, 2, 3, 4, 5, 6], 1), 0)

    ___ test_foldl_sub
        assertEqual(list_ops.foldl(operator.sub, [1, 2, 3, 4, 5], 0), -15)

    # tests for foldr
    ___ test_foldr_sub
        assertEqual(list_ops.foldr(operator.sub, [1, 2, 3, 4, 5], 0), 3)

    ___ test_foldr_add_str
        assertEqual(
            list_ops.foldr(operator.add,
                           ["e", "x", "e", "r", "c", "i", "s", "m"], "!"),
            "exercism!")

    # tests for flatten
    ___ test_flatten_nested
        assertEqual(list_ops.flat([[[1, 2], [3]], [[4]]]), [1, 2, 3, 4])

    ___ test_flatten_once
        assertEqual(list_ops.flat([["x", "y", "z"]]), ["x", "y", "z"])

    ___ test_flatten_empty
        assertEqual(list_ops.flat([]), [])

    # tests for concat
    ___ test_concat_two
        assertEqual(
            list_ops.concat([1, 3, 5, 8], [9, 4, 5, 6]),
            [1, 3, 5, 8, 9, 4, 5, 6])

    ___ test_concat_nothing
        assertEqual(
            list_ops.concat( 'orange', 'apple', 'banana' , N..),
            ["orange", "apple", "banana"])

    ___ test_concat_empty
        assertEqual(list_ops.concat([], []), [])


__ _____ __ _____
    unittest.main()
