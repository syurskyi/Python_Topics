# # [1, 3, 2, -2, 4, 5] => [1, 3, 2] [4, 5] = 9 => 4, 5
# # [] = - 1                  6
# # [-1, -3] = -1
# # [2] = 0 0
# # [-1, 2] = 1 1
#
# # break it down
#
# ___ max_sub_array l
#     index_start _ 0
#     index_end _ 0
#     sum_of_sub_array _ 0
#     new_sub_array_start _ 0
#     sum_of_new_sub_array _ 0
#     ___ index val __ en.. ?
#         __ v.. < 0:
#             # figure out the sum
#             __ s.. < s..
#                 #swap subarray indexes
#                 i.. _ n..
#                 i.. _ i.. - 1
#                 s.. _ s..
#                 s.. _ 0
#             n.. _ i.. + 1
#         ____
#             s.. +_ v..
#
#     __ s.. < s..
#         #swap subarray indexes
#         i.. _ n...
#         i.. _ le. ? - 1
#         s.. _ s..
#
#     __ s.. __ 0
#         print(-1)
#     ____
#         print i.. i..
#
# ?([2])
#
