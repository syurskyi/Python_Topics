# # Next Permutation
# # Question: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# # If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# # The replacement must be in-place, do not allocate extra memory.
# # Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# # 1,2,3 → 1,3,2
# # 3,2,1 → 1,2,3
# # 1,1,5 → 1,5,1
# # Solutions:
#
#
# c_ Solution
#     # @param num, a list of integer
#     # @return a list of integer
#     ___ nextPermutation  num
#         back _ le. ? - 2
#         w___ ? >_ 0
#             front _ le. ? - 1
#             w___ ? > ?
#                 __ ? ? < ? ?
#                     # Rule breaker found.
#                     ? ? ? ? _ ? ? ? ?
#                     ? ? + 1| _ s.. ? ? + 1|
#                     r_ ?
#                 ____
#                     ? -_ 1
#             ? -_ 1
#         ?.s..
#         r_ ?
#
#
# ? .? [1,2,3]