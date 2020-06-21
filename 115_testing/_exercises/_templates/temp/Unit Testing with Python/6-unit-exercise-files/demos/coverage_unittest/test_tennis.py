
____ tennis ______ tennis_score


______ u__

____ tennis ______ tennis_score

test_case_data _ \
{   "even_scores" :                     [("Love-All", 0, 0), 
                                         ("Fifteen-All", 1, 1),
                                         ("Thirty-All", 2, 2),
                                        ],
    "early_games_with_uneven_scores" :  [("Love-Fifteen", 0, 1),
                                         ("Fifteen-Love", 1, 0),
                                         ("Thirty-Fifteen", 2, 1),
                                         ("Forty-Thirty", 3, 2),
                                        ],
    "endgame_with_uneven_scores":       [("Advantage Player 1", 4, 3),
                                         ("Advantage Player 1", 13, 12), 
                                        ],
    "endgame_with_even_scores":         [("Deuce", 3, 3),
                                         ("Deuce", 4, 4),
                                         ("Deuce", 14, 14),  
                                        ],
    "there_is_a_winner":                [("Win for Player 1", 4, 0),
                                         ("Win for Player 2", 2, 4),
                                         ("Win for Player 1", 6, 4),
                                        ],

}

___ tennis_test_template(*args
    ___ foo
        assert_tennis_score(*args)
    r_ foo

c_ TennisTest?.?

    ___ assert_tennis_score  expected_score, player1_points, player2_points
        aE..(expected_score, tennis_score(player1_points, player2_points))


___ behaviour, test_cases __ test_case_data.items(
    ___ tennis_test_case_data __ test_cases:
        expected_output, player1_score, player2_score _ tennis_test_case_data
        test_name _ "test_{0}_{1}_{2}".f..(behaviour, player1_score, player2_score)
        tennis_test_case _ tennis_test_template(*tennis_test_case_data)
        setattr(TennisTest, test_name, tennis_test_case)




