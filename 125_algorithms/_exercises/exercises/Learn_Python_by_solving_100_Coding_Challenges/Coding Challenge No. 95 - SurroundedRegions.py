# # Surrounded Regions
# # Question: Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# # A region is captured by flipping all 'O's into 'X's in that surrounded region.
# # For example:
# # X X X X
# # X O O X
# # X X O X
# # X O X X
# # After running your function, the board should be:
# # X X X X
# # X X X X
# # X X X X
# # X O X X
# # Solutions:
#
#
# ______ co..
#
#
# c_ Solution
#     ___ solve board
#         __ ? __   # list:
#             r_   # list
#         lineNum _ le. ?
#         colNum _ le. ? 0
#         queue _ c__.d..
#         visited _ F.. ___ j __ ra.. c.. ___ i __ ra.. l..
#         ___ i __ ra.. c..
#             __ ? 0 ? __ 'O'
#                 q__.ap.. 0 ?
#             __ ? l.. - 1 ? __ 'O'
#                 q__.ap.. l.. - 1 ?
#         ___ i __ ra.. 1 l.. - 1
#             __ ? ? 0 __ 'O'
#                 q__.ap.. ? 0
#             __ ? ? c.. - 1 __ 'O'
#                 q__.ap.. ? c.. - 1
#         w___ q..
#             t _ q__.p..
#             __ ? ? 0 ? 1 __ 'O': ? ? 0 ? 1 _ '$'
#             v.. ? 0 ? 1 _ T..
#             __ ? 0 + 1 < l.. an. ? ? 0 + 1 ? 1 __ 'O' an. v.. ? 0  + 1  ? 1 __ F..
#                 q__.ap.. ? 0  + 1, ? 1
#             __ ? 0  - 1 >_ 0 an. ? ? 0  - 1  ? 1 __ 'O' an. v.. ? 0  - 1  ? 1 __ F..
#                 q__.ap.. ? 0  - 1, ? 1
#             __ ? 1  + 1 < c.. an. ? ? 0 ? 1  + 1  __ 'O' an. v.. ? 0 ? 1  + 1  __ F..
#                 q__.ap.. ? 0  ? 1  + 1
#             __ ? 1  - 1 >_ 0 an. ? ? 0 ? 1  - 1  __ 'O' an. v.. ? 0 ? 1  - 1  __ F..
#                 q__.ap.. ? 0 , ? 1  - 1
#         ___ i __ ra.. l..
#             ___ j __ ra.. c..
#                 __ ? ?  ?  __ 'O'
#                     ? ?  ?  _ 'X'
#                 __ ? ?  ?  __ '$'
#                     ? ?  ?  _ 'O'
#         r_ ?
#
#
# Solution .solve [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"], "X","O","X","X"]]