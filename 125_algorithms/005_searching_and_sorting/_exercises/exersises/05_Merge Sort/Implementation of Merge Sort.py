# # Implementation of Merge Sort
# # Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
# # Resources for Review
# # Check out the resources below for a review of Merge sort!
# #     Wikipedia
# #     Visual Algo
# #     Sorting Algorithms Animcation with Pseudocode
#
# ___ merge_sort arr
#
#     __ le. ? > 1
#         mid _ le. ? /2
#         lefthalf _ ?|;?
#         righthalf _ ?|?;
#
#         ? ?
#         ? ?
#
#         i_0
#         j_0
#         k_0
#         w__ i < le. ? an. j < le. ?
#             __ ?|? < ?|?
#                 ?|k_?|?
#                 i _ ? + 1
#             ____
#                 ?|k _ ?|?
#                 j _ ? + 1
#             k _ ? + 1
#
#         w__ i < le. ?
#             ?|k _ ?|?
#             i _ ? + 1
#             k _ ? + 1
#
#         w__ j < le. ?
#             ?|k _ ?|?
#             j _ ? + 1
#             k _ ? + 1
#
# arr = [11,2,5,4,7,6,8,1,23]
# ? ?
# ?
# # [1, 2, 4, 5, 6, 7, 8, 11, 23]
# #
# # Good Job!