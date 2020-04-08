# ______ ra..
#
# ___ quicksort lst low high
#     # If the interval [low, high] is valid
#     __ ? < ?
#         # Partition the list and get the partitioning index.
#         pivot_index _ ? ? ? ?
#
#         # Sort the elements in the list
#         # that come before and after the partition
#         ? ? ? ? - 1
#         ? ? ? + 1 ?
#
# ___ random_pivot_partition lst low high
#     # Generate a random index to select
#     # an element randomly
#     random_index _ ra__.r_r.. ? ?
#     # Swap that random element with the last
#     # element in the list (the element that would have
#     # been used as the pivot). Now the random element
#     # will be used as the pivot.
#     ?|h.. ?|r.. _ ?|r.. ?|h..
#     r_ p.. ? ? ?
#
# # Using Lomuto's Partition Scheme
# ___ partition lst low high
#     # Pivot
#     pivot _ ?|h..
#
#     i _ l.. - 1
#
#     ___ j __ ra.. ? ?
#         # If the current element is smaller than
#         # or equal to pivot
#         __ ?|? <_ ?
#             # Increment index
#             i +_ 1
#             ?|? ?|? _ ?|? ?|?
#
#     ?|?+1 ?|h.. _ ?|h.. ?|?+1
#     r_ ? + 1
