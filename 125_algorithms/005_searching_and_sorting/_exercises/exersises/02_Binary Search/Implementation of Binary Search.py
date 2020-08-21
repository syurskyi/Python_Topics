# # Implementation of Binary Search
# #
# # In this notebook we will just implement two versions of a simple binary search. View the video lecture for
# # a full breakdown!
# # Binary Search
#
# ___ binary_search arr ele
#
#     # First and last index values
#     first _ 0
#     last _ le. a.. - 1
#
#     found _ F..
#
#
#     w__ f.. <_ l.. an. no. f..
#
#         mid _  ? + ? /2 # or // for Python 3
#
#         # Match found
#         __ a..|m.. __ e..
#             f.. _ T..
#
#         # Set new midpoints up or down depending on comparison
#         e..
#             # Set down
#             __ e.. < a..|m..
#                 l.. _ m.. -1
#             # Set up
#             ____
#                 f.. _ m.. + 1
#
#     r_ f..
#
# # # list must already be sorted!
# arr _ [1,2,3,4,5,6,7,8,9,10]
#
# ? ? 4
# # True
# #
# ? ? 2.2
# # False
# #
# # Recursive Version of Binary Search
#
# ___ rec_bin_search arr ele
#
#     # Base Case!
#     __ le. ? __ 0
#         r_ F..
#
#     # Recursive Case
#     ____
#
#         mid _ le. ?/2
#
#         # If match found
#         __ ?|m..__e..
#             r_ T..
#
#         ____
#
#             # Call again on second half
#             __ e.. < ?|m..
#                 r_ ? ?|;m.. e..
#
#             # Or call on first half
#             ____
#                 r_ ? ?|m.. + 1; e..
#
# ?(?,3)
# # True
# #
# ?(?,15)
# # False
# #
# # Good Job!