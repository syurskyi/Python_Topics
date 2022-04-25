# ____ ? _______ ? ?
#
# alice ? 'alice'
# bob ? 'bob'
# tim ? 'tim'
#
# transactions
#     ? g.._alice, p.._1
#     ? g.._bob, p.._2
#     ? g.._tim, p.._3
#     ? g.._tim, p.._4
#     ? g.._alice, p.._2
#
#
#
# ___ test_init
#     ... ?.n.. __ 'alice'
#     ... ?.n.. __ 'bob'
#     ... ?.n.. __ 'tim'
#     ... ?._? __   # list
#     ... ?._? __   # list
#     ... ?._? __   # list
#
#
# ___ test_adding_karma
#     b.. + ? 0
#     ... ?.k.. __ 1
#     a.. + ? 1
#     ... ?.k.. __ 2
#     b.. + ? 2
#     ... ?.k.. __ 4
#     a.. + ? 3
#     ... a...k.. __ 6
#     t.. + ? 4
#     ... ?.k.. __ 2
#
#
# ___ test_upvotes_property
#     ... b__.p.. __ 1, 3
#     ... a__.p.. __ 2, 4
#     ... t__.p.. __ 2
#
#
# ___ test_fans_property
#     ... t__.f.. __ 1
#     ... b__.f.. __ 2
#     ... a__.f.. __ 2
#
#
# ___ test_str_dunder
#     ... s.. ? __ tim has a karma of 2 and 1 fan
#     ... s.. ? __ alice has a karma of 6 and 2 fans
#     ... s.. ? __ bob has a karma of 4 and 2 fans