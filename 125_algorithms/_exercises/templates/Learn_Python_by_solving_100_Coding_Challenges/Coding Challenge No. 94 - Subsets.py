# # Subsets
# # Question: Given a set of distinct integers, nums, return all possible subsets.
# # Note: The solution set must not contain duplicate subsets.
# # For example: If nums = [1,2,3], a solution is:
# # [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ].
# # Solutions:
#
#
# c_ Solution
#     # @param {integer[]} nums
#     # @return {integer[][]}
#     ___ subsets  nums
#         __ ? __ N..
#             r_   # list
#         result _   # list
#         ?.s..
#         ? ? 0,   # list, result)
#         r_ ?
#
#     ___ dfs  nums pos list_temp ret
#         # append new object with []
#         r__.ap..   # list + list_temp)
#         ___ i __ ra.. pos le. ?
#             l__.ap.. ? ?
#             ? ? ? + 1 ? ?
#             l__.p..
#
#
# ? .? [1,2,3]