# # Implementation of Shell Sort
# #
# # The shell sort improves on the insertion sort by breaking the original list into a number of smaller sublists,
# # each of which is sorted using an insertion sort. The unique way that these sublists are chosen is the key to
# # the shell sort. Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i,
# # sometimes called the gap, to create a sublist by choosing all items that are i items apart.
# # Resources for Review
# # Check out the resources below for a review of Shell sort!
# #     Wikipedia
# #     Visual Algo
# #     Sorting Algorithms Animcation with Pseudocode
#
# ___ shell_sort arr
#     sublistcount _ le. ? / 2
#
#     # While we still have sub lists
#     w__ ? > 0
#         ___ start __ ra.. ?
#             # Use a gap insertion
#             ? ? ? ?
#
#
#
#         ? = ? / 2
#
# ___ gap_insertion_sort arr start gap
#     ___ i __ ra.. s.. + g.. le. ? ?
#
#         currentvalue _ ?|?
#         position _ i
#
#         # Using the Gap
#         w__ ? >_ ? an. ?|? - ? > c..
#             ?|p.. _ ?|p.. - g..
#             p.. _ ? - ?
#
#         # Set current value
#         ?|p.. _ c..
#
# arr = [45,67,23,45,21,24,7,2,6,4,90]
# ? ?
# ?
#
# # [2, 4, 6, 7, 21, 23, 24, 45, 45, 67, 90]
# #
# # Good Job!