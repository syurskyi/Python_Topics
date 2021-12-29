# # 4 Sum
# # Question: Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# # Find all unique quadruplets in the array which gives the sum of target.
# # Note:
# # Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# # The solution set must not contain duplicate quadruplets.
# # For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# # A solution set is: (-1, 0, 0, 1); (-2, -1, 1, 2); (-2, 0, 0, 2)
# # Solutions:
#
#
# c_ Solution
#     ___ fourSum  nums target
#         answer _   # list
#         ?.s..
#         length _ le. ?
#         ___ k __ ra.. ? - 3
#             __ ? ? + ? ? + 1 + ? ? + 2 + ? ? + 3 > t..
#                 b..
#             ___ i __ ra.. ? + 1 l.. - 2
#                 low _ ? + 1
#                 high _ l.. - 1
#                 w___ ? < ?
#                     temp _ ? ? + ? ? + ? ? + ? ?
#                     __ t.. __ t..
#                         ans _ ? ? ? ? ? ? ? ?
#                         ?.s..
#                         l.. _ ? + 1
#                         h.. _ ? - 1
#                         __ a.. no. __ a..
#                             a__.ap.. a..
#                         w___ ? < ? an. ? ? + 1 __ ? ? ##speed up, jump the same value
#                             h.. -_ 1
#                         w___ ? < ? an. ? ? __ ? ? - 1
#                             l.. +_ 1
#                     ____ t.. > t..
#                         h.. _ ? -1
#                     ____
#                         l.. _ ? + 1
#         r_ ?
#
#
# ? .? [1, 0, -1, 0, -2, 2], 0