# # First Positive
# # Question: Given an unsorted integer array, find the first missing positive integer.
# # For example:
# # Given [1,2,0] return 3,
# # and [3,4,-1,1] return 2.
# # Solutions:
#
#
# c_ Solution
#     # @param A, a list of integers
#     # @return an integer
#     # @a very subtle solution
#     ___ firstMissingPositive A
#         n _ le. ?
#         ___ i __ ra.. ?
#             __ ? ? <_ 0: ? ? _ ? + 2
#         ___ i __ ra.. ?
#             __ ab. ? ? <_ ?
#                 curr _ ab. ? ? - 1
#                 ? ? _-ab. ? ?
#         ___ i __ ra.. ?
#             __ ? ? > 0: r_ ? + 1
#         r_ ? + 1
#
#
# ?.? [3,4,-1,1]