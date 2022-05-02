_______ unittest

____ sublist _______ check_lists, SUBLIST, SUPERLIST, EQUAL, UNEQUAL


c_ SublistTest(unittest.TestCase
    ___ test_empty_lists
        assertEqual(EQUAL, check_lists(   # list, []

    ___ test_empty_list_within
        assertEqual(SUBLIST, check_lists(   # list, [1, 2, 3]

    ___ test_within_empty_list
        assertEqual(SUPERLIST, check_lists([1],    # list

    ___ test_equal_lists
        l1 [0, 1, 2]
        l2 [0, 1, 2]
        assertEqual(EQUAL, check_lists(l1, l2

    ___ test_different_lists
        l1 l.. r.. 1000000
        l2 l..(r..(1, 1000001
        assertEqual(UNEQUAL, check_lists(l1, l2

    ___ test_false_start
        l1 [1, 2, 5]
        l2 [0, 1, 2, 3, 1, 2, 5, 6]
        assertEqual(SUBLIST, check_lists(l1, l2

    ___ test_consecutive
        l1 [1, 1, 2]
        l2 [0, 1, 1, 1, 2, 1, 2]
        assertEqual(SUBLIST, check_lists(l1, l2

    ___ test_sublist_at_start
        l1 [0, 1, 2]
        l2 [0, 1, 2, 3, 4, 5]
        assertEqual(SUBLIST, check_lists(l1, l2

    ___ test_sublist_in_middle
        l1 [2, 3, 4]
        l2 [0, 1, 2, 3, 4, 5]
        assertEqual(SUBLIST, check_lists(l1, l2

    ___ test_sublist_at_end
        l1 [3, 4, 5]
        l2 [0, 1, 2, 3, 4, 5]
        assertEqual(SUBLIST, check_lists(l1, l2

    ___ test_at_start_of_superlist
        l1 [0, 1, 2, 3, 4, 5]
        l2 [0, 1, 2]
        assertEqual(SUPERLIST, check_lists(l1, l2

    ___ test_in_middle_of_superlist
        l1 [0, 1, 2, 3, 4, 5]
        l2 [2, 3]
        assertEqual(SUPERLIST, check_lists(l1, l2

    ___ test_at_end_of_superlist
        l1 [0, 1, 2, 3, 4, 5]
        l2 [3, 4, 5]
        assertEqual(SUPERLIST, check_lists(l1, l2

    ___ test_large_lists
        l1 l..(r..(1000 * 1000 + l..(r..(1000, 1100
        l2 l..(r..(900, 1050
        assertEqual(SUPERLIST, check_lists(l1, l2

    ___ test_spread_sublist
        multiples_of_3 l..(r..(3, 200, 3
        multiples_of_15 l..(r..(15, 200, 15
        assertEqual(UNEQUAL,
                         check_lists(multiples_of_15, multiples_of_3

    ___ test_avoid_sets
        assertEqual(UNEQUAL, check_lists([1, 3], [1, 2, 3]
        assertEqual(UNEQUAL, check_lists([1, 2, 3], [1, 3]
        assertEqual(UNEQUAL, check_lists([1, 2, 3], [3, 2, 1]


__ _____ __ _____
    unittest.main()
