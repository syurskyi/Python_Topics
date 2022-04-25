# ____ ?.m.. _______ p..
# _______ r__
#
# _______ p__
#
# ____ ? _______ ? ?
#
#
# $p.. .o.. r__ 'randint'
# ___ test_get_random_number m
#     ?.r.. 17
#     ... ? __ 17
#
#
# $p.. "builtins.input", s.._ 11, '12', 'Bob', 12, 5, -1, 21, 7, N..
# ___ test_guess inp
#     game ?
#     # good
#     ... ?.g.. __ 11
#     ... ?.g.. __ 12
#     # not a number
#     w__ p__.r..(V...
#         ?.g..
#     # already guessed 12
#     w__ p__.r.. V...
#         ?.g..
#     # good
#     ... ?.g.. __ 5
#     # out of range (x2)
#     w__ p__.r.. V...
#         ?.g..
#     w__ p__.r.. V...
#         ?.g..
#     # good
#     ... ?.g.. __ 7
#     # hitting enter / no input
#     w__ p__.r.. V...
#         ?.g..
#
#
# ___ test_validate_guess capfd
#     """pytest capture stdout:
#        https://docs.pytest.org/en/2.9.1/capture.html"""
#     ? ?
#     ?._? 2
#
#     ... n.. ?._? 1
#     out, _ ?.r..
#     ... ?.r.. __ '1 is too low'
#
#     ... n.. ?._? 3
#     out, _ ?.r..
#     ... ?.r.. __ '3 is too high'
#
#     ... ?._? 2
#     out, _ ?.r..
#     ... ?.r.. __ '2 is correct!'
#
#
# $p.. "builtins.input", s.._ 4, 22, 9, 4, 6
# ___ test_game_win inp capfd
#     ? ?
#     ?._? 6
#
#     ?
#     ... ?._? __ T..
#
#     out, _ ?.r..
#     e..   '4 is too low', 'Number not in range',
#                 '9 is too high', 'Already guessed',
#                 '6 is correct!', 'It took you 3 guesses'
#
#     output line.s.. ___ ? __ ?.s.. '\n' __ ?.s..
#     ___ line exp __ z.. ?  e..
#         ... ? __ ?
#
#
# $p.. "builtins.input" s.._ N.. 5, 9, 14, 11, 12
# ___ test_game_loseinp capfd
#     ? ?
#     ?._? 13
#
#     ?
#     ... ?._? __ F..
#
#     out, _ ?.r..
#     e..  'Please enter a number', '5 is too low',
#                 '9 is too low', '14 is too high',
#                 '11 is too low', '12 is too low',
#                 'Guessed 5 times, answer was 13'
#
#     output line.s.. ___ ? __ ?.s.. '\n' __ ?.s..
#     ___ line exp __ z.. ?  e..
#         ... ? __ ?