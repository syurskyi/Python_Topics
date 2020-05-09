______ unittest


c_ IncrementTest(unittest.TestCase):
    ___ setUp
        my_dict _ {'one': 1, 'two': 2}

    ___ test_del
        del my_dict['one']
        assertNotIn('one', my_dict)

    ___ test_keys
        assertEqual(set(my_dict.keys()), {'one', 'two'})
