# ____ c.. _______ C..
#
# _______ p__
#
# ____ ? _______ ?
#
#
# ?p__.f.. s.._"module"
# ___ deck
#     r.. l.. ?
#
#
# ?p__.f.. s.._"module"
# ___ small_deck
#     r.. l.. ?(4
#
#
# ?p__.f.. s.._"module"
# ___ big_deck
#     r.. l.. ? 16
#
#
# ___ test_deck_size deck small_deck big_deck
#     ... l.. ? __ 32
#     ... l.. ? __ 16
#     ... l.. ? __ 64
#
#
# ___ test_number_action_cards deck small_deck big_deck
#     ... s.. 1 ___ c.. __ d.. __ c__.a.. __ n.. N.. __ 8
#     ... s.. 1 ___ c.. __ d.. __ c__.a.. __ N.. __ 24
#
#     ... s.. 1 ___ c.. __ s.. __ c__.a.. __ n.. N.. __ 4
#     ... s.. 1 ___ c.. __ s.. __ c__.a.. __ N.. __ 12
#
#     ... s.. 1 ___ c.. __ b.. __ c__.a.. __ n.. N.. __ 16
#     ... s.. 1 ___ c.. __ b.. __ c__.a.. __ N.. __ 48
#
#
# ___ test_all_action_cards_used deck small_deck big_deck
#     cards c__.a.. ___ c.. __ d.. __ c__.a.. __ n.. N..
#     ... s.. C.. ?.v.. __ 8
#
#     cards c__.a.. ___ c.. __ s.. __ c__.a.. __ n.. N..
#     ... s.. C.. ?.v.. __ 4
#
#     cards c__.a.. ___ c.. __ b.. __ c__.a.. __ n.. N..]
#     ... s.. C.. ?.v.. __ 16
#
#
# ___ test_action_cards_in_different_positions deck
#     action_cards c__.c__ ___ c.. __ ? __ c__.a.. __ n.. N..
#
#     deck2 l.. ?
#     action_cards2 c__.c__ ___ c.. __ ? __ c__.a.. __ n.. N..
#     ... ? !_ ?
#
#     deck3 l.. ?
#     action_cards3 c__.c__ ___ c.. __ ? __ c__.a.. __ n.. N..
#     ... ? !_ ? !_ ?
#
#
# ___ test_deck_cards_numbers_constant deck s.. big_deck
#     ___ i __ l.. 'ABCDEFGH'
#         ... s.. 1 ___ c.. __ d.. __ c__.c__ 0 __ ? __ 4
#     ___ i __ l.. 'ABCD'
#         ... s.. 1 ___ c.. __ s.. __ c__.c__ 0 __ ? __ 4
#     ___ i __ l.. 'ABCDEFGHIJKLMNOP'
#         ... s.. 1 ___ c.. __ b.. __ c__.c.. 0 __ ? __ 4
#
#
# ___ test_deck_numbers_used
#     ___ i __ r.. 1 27
#         deck l.. c.. ?
#         ... s.. 1 ___ c.. __ d.. __ i.. c__.c__ 1| __ 1 __ ?
#
#
# ___ test_out_of_bound_arg
#     w__ p__.r.. V...
#         c.. n_27