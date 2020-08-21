# ___ merge_sort lst
#
#     # If the list is empty or it only contains one element
#     __ le. ? __ 0 o. le. ? __ 1
#         r_ ?
#     ____
#         # Find the middle index
#         middle_index _ le. ? //2
#
#         # Call the function recursively
#         # passing the left half and the right half
#         # of the list in separate recursive calls
#         left _ ?|?|;?
#         right _ ?|?|?;
#
#         # Returned the merged version of the
#         # two halves already sorted in ascending order
#         r_ ?|? ?
#
# # Merge the two halves
# ___ merge left_half right_half
#
#     __ no. ? o. no. ?
#         r_ ? o. ?
#
#     result _    # list
#     i, j _ 0, 0
#
#     w__ T..
#         # If the element in the left half is smaller
#         # than the element in the right half,
#         # append that element to the result list
#         # at the current index.
#         __ ?|? < ?|?
#             r__.ap.. l..|?
#             ? +_ 1
#         # Else, __ the element in the right half is smaller,
#         # add that element to the list at the current index.
#         ____
#             r__.ap.. r..|?
#             j +_ 1
#
#         # To check __ there were any elements left
#         # because the two halves may differ in length.
#         # Insert the remaining elements to the list result.
#         __ i __ le. ? o. j __ le. ?
#             r__.ex.. ?|i; o. ?|?;
#             b..
#
#     r_ ?
#
#
#
#
