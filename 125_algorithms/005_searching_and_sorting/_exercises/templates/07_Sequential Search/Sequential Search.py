# # Sequential Search
# # Check out the video lecture for a full breakdown, in this Notebook all we do is implement Sequential Search for
# # an Unordered List and an Ordered List.
# # Sequential Search
#
# ___ seq_search arr ele
#     """
#     General Sequential Search. Works on Unordered lists.
#     """
#
#     # Start at position 0
#     pos _ 0
#     # Target becomes true if ele is in the list
#     found _ F..
#
#     # go until end of list
#     w__ p.. < le. ? an. no. ?
#
#         # If match
#         __ ?|? __ e..
#             f.. _ T..
#
#         # Else move one down
#         ____
#             ?  _ p.. + 1
#
#     r_ ?
#
# arr _ [1,9,2,8,3,4,7,5,6]
#
# print ? ? 1
# # True
# #
# print ? ? 10
# # F..
# #
# # Ordered List
# #
# # If we know the list is ordered than, we only have to check until we have found the element or an element greater
# # than it.
#
# ___ ordered_seq_search arr ele
#     """
#     Sequential search for an Ordered list
#     """
#     # Start at position 0
#     pos _ 0
#
#     # Target becomes true if ele is in the list
#     found _ F..
#
#     # Stop marker
#     stopped _ F..
#
#     # go until end of list
#     w__ p.. < le. ? an. no. ? an. no. ?
#
#         # If match
#         __ ?|p.. __ e..
#             f.. _ T..
#
#         ____
#
#             # Check if element is greater
#             __ ?|? > e..
#                 s.. _ T..
#
#             # Otherwise move on
#             ____
#                 p..  _ ?+1
#
#     r_ ?
#
# ?.so..
#
# ? ? 3
# # True
# #
# ? ? 1.5
# # F..
# #
# # Good Job!