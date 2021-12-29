# # N Queens
# # Question: The N-queens puzzle is the problem of placing n queens on an NxN chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the N-queens puzzle. Each solution contains a distinct board configuration of the N-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# # Solutions:
#
#
# c_ Solution
#     # @return a list of lists of string
#     ___ solveNQueens n
#         ___ check k j board
#             ___ i __ ra.. k
#                 __ b.. ?__ j o. ab. k-i__abs b.. ? - j
#                     r_ F..
#             r_ T..
#
#         ___ dfs depth board valuelist solution
#             #for i in range(len(board)):
#             __ ? __ le. ?
#                 s__.ap.. v..
#             ___ row __ ra.. le. b..
#                 __ check d.. ? b..
#                     s_'.'*le. b..
#                     b.. d.. _ ?
#                     ? ? + 1 ? ? + s |r.. + 'Q' + s ? + 1| s..
#         board _ -1 ___ i __ ra.. n
#         solution_  # list
#         ? 0 b..  # list,solution)
#         r_ ?
#
#
# ? .? 4