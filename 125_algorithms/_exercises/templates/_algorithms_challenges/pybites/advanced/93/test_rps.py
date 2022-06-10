# ____ ?.m.. _______ p..
#
# _______ p__
#
# ____ ? _______ _? g..
#                  l.. w.. t..
#                  d..
#                  _g..
#
#
# ?p__.f..
# ___ my_game
#     """Initialize game and move it to point where to
#        receive first player (send) input"""
#     gen g..
#     n.. ?
#     r.. ?
#
#
# $p.. >._?
# ___ test_win computerMoveMock my_game capfd
#     ?.r.. rock
#     ?.s.. paper
#     output ?.r .. 0 .s..
#     ... ? __ w__.f.. paper', 'rock
#
#
# $p.. ?._g..
# ___ test_lose computerMoveMock my_game capfd
#     ?.r.. rock
#     m__.s.. scissors
#     output ?.r .. 0 .s..
#     ... ? __ l__.f.. rock  scissors
#
#
# $p.. ?._g..
# ___ test_tie computerMoveMock my_game capfd
#     ?.r.. paper
#     ?.s.. paper
#     output ?.r .. 0 .s..
#     ... ? __ t..
#
# $p.. ?._g..
# ___ test_invalid_choice computerMoveMock my_game capfd
#     m__.s.. spam
#     output ?.r .. 0 .s..
#     ... 'Invalid' __ ?
#
#
# ?p__.m__.p. "player1, player2, result", [
#     ('scissors', 'paper', 'lose'),
#     ('paper', 'scissors', 'win'),
#     ('rock', 'paper', 'win'),
#     ('paper', 'rock', 'lose'),
#     ('rock', 'scissors', 'lose'),
#     ('scissors', 'rock', 'win'),
#     ('rock', 'rock', 'tie'),
#     ('scissors', 'scissors', 'tie'),
#     ('paper', 'paper', 'tie'),
#
# ___ test_get_winner player1 player2 result
#     ... r.. __ _? ? ?
#
#
# ___ test_stop_iteration my_game
#     # 3.6 = StopIteration
#     # 3.7 = RuntimeError - see: https://bugs.python.org/issue32670
#     w__ p__.r.. S..,R..
#         ?.s.. 'q'
#
#
# ___ test_computer_move
#     computer_moves s..
#     ___ i __ r.. 1000
#         ?.a.. _?
#     ... ? __ d__.k..
