# _______ p__
#
# ____ ? _______ ?
#
# CONGRATS_MSG ('Congrats, you earned {score} points '
#                 'obtaining the PyBites Ninja {rank} Belt')
# NEW_SCORE_MSG 'Set new score to {score}'
#
#
# ?p__.f.. s.._"module"
# ___ ninja
#     """Make a module scope ninja object (save state
#        between tests)"""
#     r.. ?
#
#
# ___ test_initial_state ninja
#     ... ?.s.. __ 0
#     ... ?._? __ N..
#
#
# ___ test_add_score_new_belt ninja capfd
#     ?.s.. 20
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._20 r.._ White __ ?
#
#
# ___ test_add_score_no_new_belt ninja capfd
#     ?.s.. 49
#     output ?.r .. 0 .s.. '\n'
#     ... N__.f.. s.._49 __ ?
#
#
# ___ test_new_score_validation ninja
#     w__ p__.r.. V...
#         ?.s.. 'a'
#         ?.s.. 40
#
#
# ___ test_add_score_another_new_belt ninja capfd
#     ?.s.. 50
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._50 r.._ Yellow __ ?
#
#
# ___ test_add_score_go_two_belts_up ninja capfd
#     ?.s.. 177
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._177 r.._ Green __ ?
#     ... ?._?.l.. __ green