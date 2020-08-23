# # This recursive version of the Binary Search
# # takes four parameters:
# # data - the list or tuple
# # low  - the lower bound
# # high - the upper bound
# # item - the item that you are looking for
# ___ binary_search data low high item
#     # If the interval is valid
#     __ ? <_ ?
#         # Find the middle of the list (index)
#         middle _ ? + ? //2
#         # If the item in the middle of the list
#         # is the one that you are looking for,
#         # return the index.
#         __ ?|? __ ?
#             r_ ?
#         # Else, if it's greater than the item that you
#         # are looking for, make a recursive call passing
#         # the middle index - 1 as upper bound to discard the
#         # upper half of the list
#         r_ ?|? > ?
#             r_ ? ? ? m.. - 1 ?
#         # Else, it it's smaller than the item that you
#         # are looking for, make a recursive call passing
#         # the middle index + 1 as lower bound to discard the
#         # lower half of the list.
#         ____
#             r_ ? ? m.. + 1 ? ?
#     # If the item is not found, return -1
#     ____
#         r_ -1
#
