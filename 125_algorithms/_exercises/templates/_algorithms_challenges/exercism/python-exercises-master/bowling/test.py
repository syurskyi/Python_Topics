______ unittest

from bowling ______ BowlingGame


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class BowlingTest(unittest.TestCase

    ___ roll(self, rolls
        [self.game.roll(roll) for roll in rolls]

    ___ roll_and_score(self, rolls
        self.roll(rolls)
        r_ self.game.score()

    ___ test_should_be_able_to_score_a_game_with_all_zeros(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 0)

    ___ test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 90)

    ___ test_a_spare_follow_by_zeros_is_worth_ten_points(self
        rolls = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 10)

    ___ test_points_scored_in_the_roll_after_a_spare_are_counted_twice(self
        rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 16)

    ___ test_consecutive_spares_each_get_a_one_roll_bonus(self
        rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 31)

    ___ test_last_frame_spare_gets_bonus_roll_that_is_counted_twice(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 17)

    ___ test_a_strike_earns_ten_points_in_a_frame_with_a_single_roll(self
        rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 10)

    ___ test_two_rolls_points_after_strike_are_counted_twice(self
        rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 26)

    ___ test_consecutive_stikes_each_get_the_two_roll_bonus(self
        rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 81)

    ___ test_strike_in_last_frame_gets_two_roll_bonus_counted_once(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 10, 7, 1]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 18)

    ___ test_rolling_spare_with_bonus_roll_does_not_get_bonus(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 10, 7, 3]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 20)

    ___ test_strikes_with_the_two_bonus_rolls_do_not_get_bonus_rolls(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 10]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 30)

    ___ test_strike_with_bonus_after_spare_in_last_frame_gets_no_bonus(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
                 3, 10]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 20)

    ___ test_all_strikes_is_a_perfect_game(self
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 300)

    ___ test_rolls_cannot_score_negative_points(self

        with self.assertRaisesWithMessage(ValueError
            self.game.roll(-1)

    ___ test_a_roll_cannot_score_more_than_10_points(self

        with self.assertRaisesWithMessage(ValueError
            self.game.roll(11)

    ___ test_two_rolls_in_a_frame_cannot_score_more_than_10_points(self
        self.game.roll(5)

        with self.assertRaisesWithMessage(ValueError
            self.game.roll(6)

    ___ test_bonus_after_strike_in_last_frame_cannot_score_more_than_10(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]

        self.roll(rolls)

        with self.assertRaisesWithMessage(ValueError
            self.game.roll(11)

    ___ test_bonus_aft_last_frame_strk_can_be_more_than_10_if_1_is_strk(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 6]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 26)

    ___ test_bonus_aft_last_frame_strk_cnt_be_strk_if_first_is_not_strk(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]

        self.roll(rolls)

        with self.assertRaisesWithMessage(ValueError
            self.game.roll(10)

    ___ test_an_incomplete_game_cannot_be_scored(self
        rolls = [0, 0]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.score()

    ___ test_cannot_roll_if_there_are_already_ten_frames(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.roll(0)

    ___ test_bonus_rolls_for_strike_must_be_rolled_before_score_is_calc(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.score()

    ___ test_both_bonuses_for_strike_must_be_rolled_before_score(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.score()

    ___ test_bonus_rolls_for_spare_must_be_rolled_before_score_is_calc(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.score()

    ___ test_cannot_roll_after_bonus_roll_for_spare(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 2]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.roll(2)

    ___ test_cannot_roll_after_bonus_rolls_for_strike(self
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 3, 2]

        self.roll(rolls)

        with self.assertRaisesWithMessage(IndexError
            self.game.roll(2)

    # Utility functions
    ___ setUp(self
        self.game = BowlingGame()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception
        r_ self.assertRaisesRegex(exception, r".+")


__ __name__ __ '__main__':
    unittest.main()
