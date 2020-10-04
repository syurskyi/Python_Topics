# # Single Number II
# # Question: Given an array of integers, every element appears three times except for one. Find that single one.
# # Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# # Solutions:
#
#
# c_ Solution
#     # @param A, a list of integer
#     # @return an integer
#     ___ singleNumber  A
#         bit _ 0 ___ i __ ra.. 32
#         ___ number __ A
#             ___ ? __ ra.. 32
#                 __  1 << ? _ ? __ 1 << ?
#                     ? ? +_ 1
#         res _ 0
#         __ ? 31 % 3 __ 0
#             ___ i __ ra.. 31
#                 __ ? ? % 3 __ 1
#                     ? +_ 1 << ?
#         ____
#             ___ ? __ ra.. 31
#                 __ ? ? % 3 __ 0: ? +_ 1 << ?
#             r.. _ - ? + 1
#         r_ ?
#
#
# ? .? [1, 2, 1, 2, 1, 2, 0, 0]