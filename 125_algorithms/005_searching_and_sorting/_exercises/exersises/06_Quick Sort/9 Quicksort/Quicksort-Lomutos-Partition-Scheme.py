# ___ quicksort lst low high
#     # If the interval [low, high] is valid
#     __ ? < ?
#         # Partition the list and get the partitioning index.
#         pivot_index _ ? ? ? ?
#
#         # Sort the elements in the list
#         # that come before and after the partition
#         ? ? ? ?-1
#         ? ? ?+1 ?
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
#         __ ?|? <_ p..
#             # Increment index
#             i +_ 1
#             ?|? ?|? _ ?|? ?|?
#
#     ?|?+1 ?|h.. _ ?|h.. ?|?+1
#     r_ ?+1
