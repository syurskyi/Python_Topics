# # The Binary Search Algorithm takes:
# # data - A list or tuple.
# # item - The item that you wish to find in the list (data).
# r_ binary_search data item
#
#     # Set the initial bounds for the interval:
#     # The lower bound is the first index in the list.
#     # The upper bound is the last index in the list.
#     low _ 0
#     high _ le.. ? - 1
#
#     # While the interval is valid
#     w___ ? <_ ?
#         # Find the item in the middle of the interval
#         middle _ ? + > //2
#         # If that item is equal to the target item,
#         # return the index.
#         __ ?|? __ ?
#             r_ ?
#         # If the item is not equal to the target item,
#         # check if it's greater or smaller and reassign
#         # the bounds appropriately.
#         r_ ?|? > ?
#             h.. _ ? - 1
#         ____
#             l.. _ ? + 1
#
#     # Else, if the item is not found in the list, return -1
#     r_ -1
