_______ unittest

____ bowling _______ BowlingGame


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

c_ BowlingTest(unittest.TestCase

    ___ roll  rolls
        [game.roll(roll) ___ roll __ rolls]

    ___ roll_and_score  rolls
        roll(rolls)
        r.. game.score()

    ___ test_should_be_able_to_score_a_game_with_all_zeros
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 0)

    ___ test_should_be_able_to_score_a_game_with_no_strikes_or_spares
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = roll_and_score(rolls)

        assertEqual(score, 90)

    ___ test_a_spare_follow_by_zeros_is_worth_ten_points
        rolls = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 10)

    ___ test_points_scored_in_the_roll_after_a_spare_are_counted_twice
        rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 16)

    ___ test_consecutive_spares_each_get_a_one_roll_bonus
        rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 31)

    ___ test_last_frame_spare_gets_bonus_roll_that_is_counted_twice
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7]

        score = roll_and_score(rolls)

        assertEqual(score, 17)

    ___ test_a_strike_earns_ten_points_in_a_frame_with_a_single_roll
        rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 10)

    ___ test_two_rolls_points_after_strike_are_counted_twice
        rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 26)

    ___ test_consecutive_stikes_each_get_the_two_roll_bonus
        rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = roll_and_score(rolls)

        assertEqual(score, 81)

    ___ test_strike_in_last_frame_gets_two_roll_bonus_counted_once
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 10, 7, 1]

        score = roll_and_score(rolls)

        assertEqual(score, 18)

    ___ test_rolling_spare_with_bonus_roll_does_not_get_bonus
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 10, 7, 3]

        score = roll_and_score(rolls)

        assertEqual(score, 20)

    ___ test_strikes_with_the_two_bonus_rolls_do_not_get_bonus_rolls
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 10]

        score = roll_and_score(rolls)

        assertEqual(score, 30)

    ___ test_strike_with_bonus_after_spare_in_last_frame_gets_no_bonus
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
                 3, 10]

        score = roll_and_score(rolls)

        assertEqual(score, 20)

    ___ test_all_strikes_is_a_perfect_game
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        score = roll_and_score(rolls)

        assertEqual(score, 300)

    ___ test_rolls_cannot_score_negative_points

        w__ assertRaisesWithMessage(ValueError
            game.roll(-1)

    ___ test_a_roll_cannot_score_more_than_10_points

        w__ assertRaisesWithMessage(ValueError
            game.roll(11)

    ___ test_two_rolls_in_a_frame_cannot_score_more_than_10_points
        game.roll(5)

        w__ assertRaisesWithMessage(ValueError
            game.roll(6)

    ___ test_bonus_after_strike_in_last_frame_cannot_score_more_than_10
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]

        roll(rolls)

        w__ assertRaisesWithMessage(ValueError
            game.roll(11)

    ___ test_bonus_aft_last_frame_strk_can_be_more_than_10_if_1_is_strk
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 6]

        score = roll_and_score(rolls)

        assertEqual(score, 26)

    ___ test_bonus_aft_last_frame_strk_cnt_be_strk_if_first_is_not_strk
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]

        roll(rolls)

        w__ assertRaisesWithMessage(ValueError
            game.roll(10)

    ___ test_an_incomplete_game_cannot_be_scored
        rolls = [0, 0]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.score()

    ___ test_cannot_roll_if_there_are_already_ten_frames
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.roll(0)

    ___ test_bonus_rolls_for_strike_must_be_rolled_before_score_is_calc
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.score()

    ___ test_both_bonuses_for_strike_must_be_rolled_before_score
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.score()

    ___ test_bonus_rolls_for_spare_must_be_rolled_before_score_is_calc
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.score()

    ___ test_cannot_roll_after_bonus_roll_for_spare
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 2]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.roll(2)

    ___ test_cannot_roll_after_bonus_rolls_for_strike
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 3, 2]

        roll(rolls)

        w__ assertRaisesWithMessage(IndexError
            game.roll(2)

    # Utility functions
    ___ setUp
        game = BowlingGame()
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
