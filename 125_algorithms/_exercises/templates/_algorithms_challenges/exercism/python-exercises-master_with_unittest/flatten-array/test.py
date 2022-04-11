_______ unittest

____ flatten_array _______ flatten


c_ FlattenArrayTests(unittest.TestCase

    ___ test_no_nesting
        assertEqual(flatten([0, 1, 2]), [0, 1, 2])

    ___ test_one_level_nesting
        assertEqual(flatten([0, [1], 2]), [0, 1, 2])

    ___ test_two_level_nesting
        assertEqual(flatten([0, [1, [2, 3]], [4]]), [0, 1, 2, 3, 4])

    ___ test_empty_nested_lists
        assertEqual(flatten([[()]]), [])

    ___ test_with_none_values
        inputs [0, 2, [[2, 3], 8, [[100]], N.., [[N..]]], -2]
        e.. [0, 2, 2, 3, 8, 100, -2]
        assertEqual(flatten(inputs), e..)

    ___ test_six_level_nesting
        inputs [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
        e.. [1, 2, 3, 4, 5, 6, 7, 8]
        assertEqual(flatten(inputs), e..)

    ___ test_all_values_are_none
        inputs [N.., [[[N..]]], N.., N.., [[N.., N..], N..], N..]
        e..    # list
        assertEqual(flatten(inputs), e..)

    ___ test_strings
        assertEqual(flatten( '0',  '1', '2']]),  '0', '1', '2' )


__ _____ __ _____
    unittest.main()
