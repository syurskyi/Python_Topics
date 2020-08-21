# ___ quicksort lst low high
#     # If the interval [low, high] is valid
#     __ ? < ?
#         # pivot_index is partitioning index,
#         # lst[pivot_index] is now at the correct index
#         pivot_index _ ? ? ? ? ?
#
#         # Sort the elements in the list
#         # that come before and after the partition
#         ? ? ? ?
#         ? ? ? + 1 ?
#
#
# # Using Hoare's Partition Scheme
# ___ partition lst low high
#     # Get the pivot element
#     pivot _ ?|l..
#
#     # Get the indices that we will be working with
#     i _ ? - 1
#     j _ ? + 1
#
#     # Indices move towards each other until they meet
#
#     w___ T..
#
#         # Move the i index to the right until we
#         # find an element that is smaller than the pivot.
#         i +_ 1
#         w___ l..|? < p..
#             i +_ 1
#
#         # Move the j index to the left until we find an element
#         # that is greater than the pivot.
#         j -_ 1
#         w___ ?|? > p..
#             j -_ 1
#
#         # If i and j did not meet before we need to make
#         # a swap, then swap the elements
#         __ i < j
#             ?|? ?|? _ ?|? ?|?
#         # If j now comes before i in the list
#         # (__ no swaps were made before they crossed)
#         # return the value of j.
#         ____
#             r_ ?
