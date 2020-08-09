______ unittest

from change ______ find_minimum_coins


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class ChangeTest(unittest.TestCase
    ___ test_single_coin_change(self
        self.assertEqual(find_minimum_coins(25, [1, 5, 10, 25, 100]), [25])

    ___ test_multiple_coin_change(self
        self.assertEqual(find_minimum_coins(15, [1, 5, 10, 25, 100]), [5, 10])

    ___ test_change_with_Lilliputian_Coins(self
        self.assertEqual(find_minimum_coins(23, [1, 4, 15, 20, 50]),
                         [4, 4, 15])

    ___ test_change_with_Lower_Elbonia_Coins(self
        self.assertEqual(find_minimum_coins(63, [1, 5, 10, 21, 25]),
                         [21, 21, 21])

    ___ test_large_target_values(self
        self.assertEqual(find_minimum_coins(999, [1, 2, 5, 10, 20, 50, 100]),
                         [2, 2, 5, 20, 20, 50, 100, 100, 100,
                          100, 100, 100, 100, 100, 100])

    ___ test_possible_change_without_unit_coins_available(self
        self.assertEqual(find_minimum_coins(21, [2, 5, 10, 20, 50]),
                         [2, 2, 2, 5, 10])

    ___ test_another_possible_change_without_unit_coins_available(self
        self.assertEqual(find_minimum_coins(27, [4, 5]),
                         [4, 4, 4, 5, 5, 5])

    ___ test_no_coins_make_0_change(self
        self.assertEqual(find_minimum_coins(0, [1, 5, 10, 21, 25]), [])

    ___ test_error_testing_for_change_smaller_than_smallest_coin(self
        with self.assertRaisesWithMessage(ValueError
            find_minimum_coins(3, [5, 10])

    ___ test_error_if_no_combination_can_add_up_to_target(self
        with self.assertRaisesWithMessage(ValueError
            find_minimum_coins(94, [5, 10])

    ___ test_cannot_find_negative_change_values(self
        with self.assertRaisesWithMessage(ValueError
            find_minimum_coins(-5, [1, 2, 5])

    # Utility functions
    ___ setUp(self
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception
        r_ self.assertRaisesRegex(exception, r".+")


__ __name__ __ "__main__":
    unittest.main()
