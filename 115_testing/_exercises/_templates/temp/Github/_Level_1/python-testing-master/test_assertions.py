____ u__ ______ TestCase


c_ TestAssertions(TestCase
    """
    Showcase for different assertions provided by the unittest library.
    These are just a few examples and do not cover every assertion method provided.
    For the full documentation see the python docs: https://docs.python.org/3/library/unittest.html
    """

    ___ test_equality
        x _ 42
        y _ 42

        aE..(x, y)
        assertNotEqual(42, 1337)

    ___ test_none_values
        x _ 42
        y _ None

        assertIsNone(None)
        assertIsNone(y)
        assertIsNotNone(x)

    ___ test_bool
        assertTrue(1 == 1)
        assertFalse(1 == 0)

    ___ test_comparison
        assertGreater(1337, 42)
        assertGreaterEqual(13, 13)
        assertLess(42, 1337)
        assertLessEqual(13, 13)
        assertAlmostEqual(2.012, 2.013, 2)
        assertNotAlmostEqual(2.012, 2.013, 3)

    ___ test_exceptions
        w__ assertRaises(ZeroDivisionError
            x _ 42 / 0

    ___ test_list_comparison
        list1 _ [1, 2, 3]
        list2 _ [1, 2, 3]
        list3 _ [3, 2, 1]
        assertListEqual(list1, list2)
        assertCountEqual(list1, list3)
        # same methods exist for strings, sequences, tuples, sets and dictionaries
