_______ unittest

____ change _______ find_minimum_coins


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

c_ ChangeTest(unittest.TestCase
    ___ test_single_coin_change
        assertEqual(find_minimum_coins(25, [1, 5, 10, 25, 100]), [25])

    ___ test_multiple_coin_change
        assertEqual(find_minimum_coins(15, [1, 5, 10, 25, 100]), [5, 10])

    ___ test_change_with_Lilliputian_Coins
        assertEqual(find_minimum_coins(23, [1, 4, 15, 20, 50]),
                         [4, 4, 15])

    ___ test_change_with_Lower_Elbonia_Coins
        assertEqual(find_minimum_coins(63, [1, 5, 10, 21, 25]),
                         [21, 21, 21])

    ___ test_large_target_values
        assertEqual(find_minimum_coins(999, [1, 2, 5, 10, 20, 50, 100]),
                         [2, 2, 5, 20, 20, 50, 100, 100, 100,
                          100, 100, 100, 100, 100, 100])

    ___ test_possible_change_without_unit_coins_available
        assertEqual(find_minimum_coins(21, [2, 5, 10, 20, 50]),
                         [2, 2, 2, 5, 10])

    ___ test_another_possible_change_without_unit_coins_available
        assertEqual(find_minimum_coins(27, [4, 5]),
                         [4, 4, 4, 5, 5, 5])

    ___ test_no_coins_make_0_change
        assertEqual(find_minimum_coins(0, [1, 5, 10, 21, 25]), [])

    ___ test_error_testing_for_change_smaller_than_smallest_coin
        w__ assertRaisesWithMessage(V...
            find_minimum_coins(3, [5, 10])

    ___ test_error_if_no_combination_can_add_up_to_target
        w__ assertRaisesWithMessage(V...
            find_minimum_coins(94, [5, 10])

    ___ test_cannot_find_negative_change_values
        w__ assertRaisesWithMessage(V...
            find_minimum_coins(-5, [1, 2, 5])

    # Utility functions
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _______ __ _______
    unittest.main()
