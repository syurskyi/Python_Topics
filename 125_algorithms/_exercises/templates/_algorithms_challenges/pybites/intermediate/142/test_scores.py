_______ p__

____ scores _______ Player, calculate_score, get_winner


?p__.m__.p.("arg, expected", [
    ([1, 3, 2, 5], 5),
    ([1, 4, 2, 5], 9),
    ([1, 1, 1, 1], 0),
    ([4, 5, 1, 2], 9),
    ([6, 6, 5, 5], 22),
])
___ test_calculate_score(arg, expected
    ... calculate_score(arg) __ expected


?p__.m__.p.("arg", [
    [4, 5, 6, 'a' ,
    [4, -5, -1, 2],
    [4, 7, 6, 2],
])
___ test_wrong_inputs(arg
    w__ p__.r..(ValueError
        calculate_score(arg)


___ test_winner_3_players
    players = [
      Player(name='player 1', scores=[1, 3, 2, 5]),
      Player(name='player 2', scores=[1, 1, 1, 1]),
      Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
    ]
    ... get_winner(players) __ players[-1]


___ test_winner_shorter_score_len_raises_exception
    players = [
      Player(name='player 1', scores=[4, 3, 5, 5]),
      Player(name='player 2', scores=[4, 4, 6]),  # lacks one score
      Player(name='player 3', scores=[4, 5, 6, 6]),
    ]
    w__ p__.r..(ValueError
        get_winner(players)


___ test_winner_longer_score_len_raises_exception
    players = [
      Player(name='player 1', scores=[4, 3, 5, 5, 4]),
      Player(name='player 2', scores=[4, 4, 6, 6, 3, 2]),  # 1 more
      Player(name='player 3', scores=[4, 5, 6, 6, 5]),
    ]
    w__ p__.r..(ValueError
        get_winner(players)