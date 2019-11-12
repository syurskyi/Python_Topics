# ___ list_sum_recursive input_list
#     # Base case
#     i_ input_list __ ||
#         r_ 0
#
#     # Recursive case
#     # Decompose the original problem into simpler instances of the same problem
#     # by making use of the fact that the input is a recursive data structure
#     # and can be deﬁned in terms of a smaller version of itself
#     e_
#         head _ i00_l00[0]
#         smaller_list = i00_l00|1:|
#         r_ head + l0_s00_r00|s00_l00|
#
# print l0_s00_r00 1 2 3
# # 6