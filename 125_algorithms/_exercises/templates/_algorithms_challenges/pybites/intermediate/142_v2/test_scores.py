# _______ p__
#
# ____ ? _______ ? ? ?
#
#
# ?p__.m__.p. "arg, expected",
#     ([1, 3, 2, 5], 5),
#     ([1, 4, 2, 5], 9),
#     ([1, 1, 1, 1], 0),
#     ([4, 5, 1, 2], 9),
#     ([6, 6, 5, 5], 22),
#
# ___ test_calculate_score arg e..
#     ... ? ? __ e..
#
#
# ?p__.m__.p. "arg",
#     [4, 5, 6, 'a' ,
#     [4, -5, -1, 2],
#     [4, 7, 6, 2],
#
# ___ test_wrong_inputs(arg
#     w__ p__.r.. V...
#         ? ?
#
#
# ___ test_winner_3_players
#     ?
#       ? name='player 1', scores=[1, 3, 2, 5]),
#       ? name='player 2', scores=[1, 1, 1, 1]),
#       ? name='player 3', scores=[4, 5, 1, 2]),  # max 9
#
#     ... ? ? __ ? -1
#
#
# ___ test_winner_shorter_score_len_raises_exception
#     ?
#       ? name='player 1', scores=[4, 3, 5, 5]),
#       ? name='player 2', scores=[4, 4, 6]),  # lacks one score
#       ? name='player 3', scores=[4, 5, 6, 6]),
#
#     w__ p__.r.. V...
#         ? ?
#
#
# ___ test_winner_longer_score_len_raises_exception
#     ?
#       ? name='player 1', scores=[4, 3, 5, 5, 4]),
#       ? name='player 2', scores=[4, 4, 6, 6, 3, 2]),  # 1 more
#       ? name='player 3', scores=[4, 5, 6, 6, 5]),
#
#     w__ p__.r.. V...
#         ? ?