# c_ Event li..
#     ___ -c $ $$
#         ___ item __ ?
#             ? $ $$
#
#
# c_ Game
#     ___ -
#         __events _ E..
#
#     ___ fire args
#         __e.. a..
#
#
# c_ GoalScoredInfo
#     ___ -  who_scored goals_scored
#         __g.. _ g..
#         __w.. _ w..
#
#
# c_ Player
#     ___ - name game
#         __?  ?
#         __?  ?
#         __goals_scored _ 0
#
#     ___ score
#         __goals_scored +_ 1
#         args _ GSI.. __n.. __g..
#         __game.fire(args)
#
#
# c_ Coach
#     ___ - game
#         ?.e___.ap.. __c..
#
#     ___ celebrate_goal args
#         __ isi.. ar.. GSI.. an. ar__.g_s.. < 3
#             print _*Coach says: well done, |ar__.w_s..!
#
#
# __ _______ __ ______
#     game _ G..
#     player _ P.. 'Sam', ?
#     coach _ C.. g..
#
#     p__.sc..  # Coach says: well done, Sam!
#     p__.sc..  # Coach says: well done, Sam!
#     p__.sc..  # ignored by coach
