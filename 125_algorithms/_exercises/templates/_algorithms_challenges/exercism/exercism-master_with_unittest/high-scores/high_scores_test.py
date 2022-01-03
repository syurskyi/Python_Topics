_______ unittest

____ high_scores _______ HighScores


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0


c_ HighScoreTest(unittest.TestCase):
    ___ test_list_of_scores
        scores = [30, 50, 20, 70]
        expected = [30, 50, 20, 70]
        assertEqual(HighScores(scores).scores, expected)

    ___ test_latest_score
        scores = [100, 0, 90, 30]
        expected = 30
        assertEqual(HighScores(scores).latest(), expected)

    ___ test_highest_score
        scores = [40, 100, 70]
        expected = 100
        assertEqual(HighScores(scores).highest(), expected)

    ___ test_top_3_scores
        scores = [50, 30, 10]
        expected = [50, 30, 10]
        assertEqual(HighScores(scores).top(), expected)

    ___ test_personal_bests_highest_to_lowest
        scores = [20, 10, 30]
        expected = [30, 20, 10]
        assertEqual(HighScores(scores).top(), expected)

    ___ test_personal_bests_when_there_is_a_tie
        scores = [40, 20, 40, 30]
        expected = [40, 40, 30]
        assertEqual(HighScores(scores).top(), expected)

    ___ test_personal_bests_when_there_are_less_than_3
        scores = [30, 70]
        expected = [70, 30]
        assertEqual(HighScores(scores).top(), expected)

    ___ test_personal_bests_when_there_is_only_one
        scores = [40]
        expected = [40]
        assertEqual(HighScores(scores).top(), expected)

    ___ test_personal_bests_from_a_long_list
        scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
        expected = [100, 90, 70]
        assertEqual(HighScores(scores).top(), expected)

    ___ test_message_for_new_personal_best
        scores = [20, 40, 0, 30, 70]
        expected = "Your latest score was 70. That's your personal best!"
        assertEqual(HighScores(scores).report(), expected)

    ___ test_message_when_latest_score_is_not_the_highest_score
        scores = [20, 100, 0, 30, 70]
        expected = (
            "Your latest score was 70. That's 30 short of your personal best!"
        )
        assertEqual(HighScores(scores).report(), expected)

    ___ test_message_for_repeated_personal_best
        scores = [20, 70, 50, 70, 30]
        expected = (
            "Your latest score was 30. That's 40 short of your personal best!"
        )
        assertEqual(HighScores(scores).report(), expected)


__ __name__ __ "__main__":
    unittest.main()
