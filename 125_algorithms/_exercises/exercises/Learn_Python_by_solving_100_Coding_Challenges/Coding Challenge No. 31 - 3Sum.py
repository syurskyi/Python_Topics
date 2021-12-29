# # 3 Sum
# # Question: Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# # Note:
# # Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# # The solution set must not contain duplicate triplets.
# # Solutions:
#
#
# c_ Solution
#     # @return a list of lists of length 3, [[val1,val2,val3]]
#     ___ threeSum  num
#         length _ le. ?
#         result _   # list
#
#         __ ? < 3
#             r_ ?
#         ?.s..
#
#         ___ i __ ra.. ? - 2
#             __ ? > 0 an. ? ? __ ? ? - 1
#                 c..
#             low _ ? + 1
#             high _ l.. - 1
#             target_gap _ 0 - ? ?
#
#             w___ ? < ?
#                 __ ? ? + ? ? < ?
#                     l.. +_ 1
#                     w___ ? < ? an. ? ? __ ? ? - 1
#                         l.. +_ 1
#                 ____ ? ? + ? ? > ?
#                     h.. -_ 1
#                     w___ ? < ? an. ? ? __ ? ? + 1
#                         h.. -_ 1
#                 ____
#                     r__.ap.. ? ? ? ? ? ?
#                     l.. +_ 1
#                     w___ ? < ? an. ? ? __ ? ? - 1
#                         l.. +_ 1
#                     h.. -_ 1
#
#                 w___ ? < ? an. ? ? __ ? ? + 1
#                     h.. -_ 1
#         r_ ?
#
#
# ? .? -1, 0, 1, 2, -1, -4