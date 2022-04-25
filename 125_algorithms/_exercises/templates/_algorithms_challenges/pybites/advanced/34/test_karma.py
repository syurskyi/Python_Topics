# _______ p__
#
# ____ ? _______ ? ?
#
#
# ?p__.f..
# ___ bob
#     r.. ? 'bob'
#
#
# ?p__.f..
# ___ tim
#     r.. ? 'tim'
#
#
# ?p__.f..
# ___ alice
#     r.. ? 'alice'
#
#
# ?p__.f..
# ___ transactions bob, tim, alice
#     r..
#         ?(g.._alice, p.._1
#         ?(g.._bob, p.._2),
#         ?(g.._tim, p.._3),
#         ?(g.._tim, p.._4),
#         ?(g.._alice, p.._2),
#
#
#
# ___ test_init transactions, bob, tim, alice
#     ... ?.n.. __ 'alice'
#     ... ?.n.. __ 'bob'
#     ... ?.n.. __ 'tim'
#     ... ?._? __   # list
#     ... ?._? __   # list
#     ... ?._? __   # list
#
#
# ___ test_scores_and_points transactions bob tim alice
#     b.. + ? 0
#     ... ?.k.. __ 1
#     a.. + ? 1
#     ... ?.k.. __ 2
#     b.. + ? 2
#     ... ?.k.. __ 4
#     a.. + ? 3
#     ... ?.k.. __ 6
#     t.. + ? 4
#     ... ?.k.. __ 2
#     # point lists at this point
#     ... b__.p.. __ 1, 3
#     ... a__.p.. __ 2, 4
#     ... t__.p.. __ 2
#
#
# ___ test_fans_property transactions bob tim alice
#     t.. + ? 4
#     ... ?.f.. __ 1
#     b.. + ? 0
#     b.. + ? 0  # same giver, does not increase fan count
#     ... ?.f.. __ 1
#     a.. + ? 1
#     a.. + ? 2
#     ... ?.f.. __ 2
#
#
# ___ test_str_dunder transactions bob tim alice
#     t.. + ? 4
#     ... s.. ? __ 'tim has a karma of 2 and 1 fan'
#     a.. + ? 1
#     a.. + ? 3
#     ... s.. ? __ 'alice has a karma of 6 and 2 fans'
