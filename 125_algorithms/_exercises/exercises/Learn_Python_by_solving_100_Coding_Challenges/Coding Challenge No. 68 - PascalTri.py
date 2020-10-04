# # Pascal's Triangle
# # Question: Given numRows, generate the first numRows of Pascal's triangle.
# # For example, given numRows = 5,
# # Return
# # [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
# # Solutions:
#
#
# c_ Solution
#     # @return a list of lists of integers
#     ___ generate numRows
#         __ numRows __ 0
#             r_   # list
#
#         result _ 1
#         w___ le. ? < ?
#             temp _ 1 # Every row starts with 1
#
#             ___ index __ ra.. le. ? -1 -1
#                 ?.ap.. ? -1 ? + ? -1 ? + 1
#
#             ?.ap.. 1 # Every row ends with 1
#             ?.ap.. ?
#
#         r_ ?
#
#
# ? .? 5
