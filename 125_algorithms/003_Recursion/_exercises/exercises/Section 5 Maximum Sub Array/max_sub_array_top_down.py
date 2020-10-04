# c_ MaxSubArrayTopDown
#     ___ - prices
#         ? ?
#         sub_solutions _ |N.. * le. ?
#
#     ___ max_sub_array
#         max_value _ 0
#         ___ j __ ra.. le. ?
#             max_value _ ma. ? ?|?
#         r_ ?
#
#     ___ max_sub_array_ending_at i
#         __ s..|? __ no. N..
#             r_ s..|?
#         __ i __ 0
#             r_ ? 0
#         m _ ma. p..|? m..|? - 1 + p..|?
#         s..|? _ m
#         r_ ?
#
#
# msa _ ? 5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3
# print ?.m..
#
# # input _ [1] * 900
# # for i in range(10):
# #     msa _ MaxSubArrayTopDown(input)
# #     print(msa.max_sub_array())
#
