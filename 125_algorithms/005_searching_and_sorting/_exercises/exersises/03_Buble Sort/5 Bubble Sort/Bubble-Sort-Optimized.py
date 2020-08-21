# ___ bubble_sort lst
#     # Number of items in the list
#     n _ le. ?
#
#     # Traverse the list
#     ___ i __ ra.. ?
#         # If the iteration causes a swap or not.
#         # By default, it's False, but if a swap
#         # occurs, it changes to True.
#         swapped _ F..
#
#         # For every unsorted element in the list
#         # (the last i elements are already sorted)
#         ___ j __ ra.. 0 ? - ? - 1
#             # If the current element is greater than
#             # the element to its right, swap them
#             __ ?|? > ?|?+1
#                 # Swapping...
#                 ?|? ?|?+1 _ ?|?+1 ?|?
#                 # A swap occured, update the variable
#                 swapped _ T..
#
#         # If the inner loop did not cause any swaps,
#         # the list is sorted, so the loop can stop.
#         __ no. ?
#             b..
