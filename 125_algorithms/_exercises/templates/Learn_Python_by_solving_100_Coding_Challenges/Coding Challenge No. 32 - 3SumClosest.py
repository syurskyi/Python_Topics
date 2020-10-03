# # 3 Sum Closest
# # Question: Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
# # target. Return the sum of the three integers. You may assume that each input would have exactly one solution
# # For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2.
# # (-1 + 2 + 1 = 2).
# # Solutions:
#
#
# c_ Solution
#     ___ threeSumClosest  numbers target
#         ?.s..
#         ans _ N..
#         ___ i __ ra.. le. ?
#             l, r _ ? + 1, le. ? - 1
#             w___  ? < ?
#                 su. _ ? ? + ? ? + ? ?
#                 __ a.. i. N.. o. ab. su.- t.. < ab. a.. - t..
#                     a.. _ su.
#                 __ su. <_ t..
#                     l _ ? + 1
#                 ____
#                     r _ ? - 1
#         r_ ?
#
#
# ? .? [-1, 2, 1, -4], 1