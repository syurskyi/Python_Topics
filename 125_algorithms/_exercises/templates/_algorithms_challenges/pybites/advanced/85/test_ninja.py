# _______ p__
#
# ____ ? _______ ?
#
# CONGRATS_MSG ('Congrats, you earned {score} points '
#                 'obtaining the PyBites Ninja {rank} Belt')
# NEW_SCORE_MSG 'Set new score to {score}'
#
#
# ?p__.f..
# ___ ninja
#     r.. ?
#
#
# ?p__.f..
# ___ white_belt
#     ninja ? s.._10
#     ?._? white
#     r.. ?
#
#
# ?p__.f..
# ___ yellow_belt
#     ninja ? s.._50
#     ?._? yellow
#     r.. ?
#
#
# ___ test_initial_state ninja
#     ... ?.score __ 0
#     ... ?._? __ N..
#
#
# ___ test_white_belt ninja capfd
#     ?.score 20
#     ... ?._? __ white
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._20 r.._ White __ ?
#
#
# ___ test_new_score_same_belt_no_congrats_msg white_belt capfd
#     ... ?.s.. __ 10
#     ?.s.. 49
#     ... ?._? __ white
#     output ?.r .. 0 .s.. '\n'
#     ... N_.f.. s.._49 __ ?
#
#
# ___ test_new_score_new_belt ninja, capfd
#     ?.s.. 50
#     ... ?._? __ yellow
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._50 r.._ Yellow __ ?
#
#
# ___ test_higher_belt ninja capfd
#     ?.s.. 177
#     ... ?._?.l.. __ green
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._177 r.._ Green __ ?
#
#
# ___ test_gt_max_score_highest_belt ninja capfd
#     ?.s.. 1010
#     ... ?._?.l.. __ red
#     output ?.r .. 0 .s.. '\n'
#     ... C__.f.. s.._1010 r.._ Red __ ?
#
#
# ___ test_new_score_should_be_int ninja
#     w__ p__.r.. V... m.._"Score takes an int"
#         ?.s.. 'a'
#
#
# ___ test_new_score_should_be_higher yellow_belt
#     ... ?.s.. __ 50
#     w__ p__.r.. V... m.._"Cannot lower score"
#         ?.s.. 40
