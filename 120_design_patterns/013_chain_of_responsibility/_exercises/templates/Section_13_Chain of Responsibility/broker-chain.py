# # 1) event broker
# # 2) command-query separation (cqs)
# # 3) observer
# ____ a.. ______ A..
# ____ e.. ______ E..
#
#
# c_ Event li..
#     ___ -c  $ $$
#         ___ item __ ?
#             ? $ $$
#
#
# c_ WhatToQuery E..
#     ATTACK _ 1
#     DEFENSE _ 2
#
#
# c_ Query
#     ___ - creature_name what_to_query default_value
#         value _ d..  # bidirectional
#         w.. _ w..
#         c.. _ c..
#
#
# c_ Game
#     ___ -
#         queries _ E..
#
#     ___ perform_query sender query
#         q.. ?
#
#
# c_ Creature
#     ___ - game name attack defense
#         initial_defense _ d..
#         initial_attack _ a..
#         n.. _ n..
#         g.. _ g..
#
#     ??
#     ___ attack
#         q _ Q.. name W__.A.. initial_attack
#         g__.p_q.. ? ?
#         r_ q.value
#
#     @property
#     ___ defense(self):
#         q _ Query(name, WhatToQuery.DEFENSE, initial_attack)
#         game.perform_query(self, q)
#         r_ ?.v..
#
#     ___ -s
#         r_ _*|n.. ||a../|d..
#
#
# c_ CreatureModifier A..
#     ___ - game, creature
#         c.. _ c..
#         g.. _ g..
#         g__.q__.ap.. h..
#
#     ___ handle sender query
#         p..
#
#     ___ -e
#         r_ ?
#
#     ___ -e
#         g__.q__.r.. h..
#
#
# c_ DoubleAttackModifier C..
#
#     ___ handle sender query
#         __ s__.n.. __ c__.n.. an.
#                 q__.w.. __ W____.A..
#             q__.v.. *_ 2
#
#
# c_ IncreaseDefenseModifier C..
#
#     ___ handle sender query
#         __ s___.n.. __ c___.n.. an.
#                 q___.w.. __ W___.D..
#             q__.v.. +_ 3
#
#
# __ _______ __ ______
#     game _ G..
#     goblin _ C.. ? 'Strong Goblin', 2, 2
#     print ?
#
#     w____ D... ?  ?
#         print go..
#         w__ I.. ? ?
#             print g..
#
#     print g..
