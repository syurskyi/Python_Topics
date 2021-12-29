# # Minimum Path Sum
# # Question: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# # Note: You can only move either down or right at any point in time.
# # Solutions:
#
# c_ Solution
#     # @param grid, a list of lists of integers
#     # @return an integer
#     ___ minPathSum  grid
#         __ le. ? __ 0 o. le. ?[0]__0
#             r_ 0
#         ___ row __ ra.. 0, le. ?
#             ___ col __ ra.. 0 le. ? 0
#                 __ ? > 0 an. ? > 0
#                     ? ? ? +_ mi. ? ? - 1 ? ? ? ? - 1
#                 ____ ? > 0
#                     ? ? ? +_ ? ? - 1 ?
#                 ____ ? > 0
#                     ? ? ? +_ ? ? ? - 1
#         r_ ? le. ? - 1 le. ? 0 -1
#
#
# grid _ [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# ? .? ?