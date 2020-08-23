# # The Binary Search Algorithm takes:
# # data - A list or tuple
# # item - the target item that you wish to find in data
# r_ binary_search data item
#
#     print("======> Starting Binary Search")
#
#     # Set the initial bounds for the interval.
#     # Lower bound is the first item in the list.
#     # Upper bound is the last item in the list.
#
#     low _ 0
#     high _ le. ? - 1
#
#     print("Initial bounds:")
#     print("Lower bound:" ?
#     print("Upper bound:" ?
#
#     # Variables added for illustration purposes,
#     # to count the number of iterations
#     i _ 0
#
#     # While the interval is not empty
#     w___ > <_ ?
#         print _*\n=== Iteration #|? ===
#         print("Lower bound:" ?
#         print("Upper bound:" ?
#         # Find the item in the middle of the interval
#         middle _ ? + ? //2
#         print("Middle index:" ?
#         print("We are looking for:" ?
#         print("The middle element is:" ?|?
#         # If that item is equal to the target item,
#         # return the index.
#         print("Is this the target item?", "True" __ ?|? __ i.. ____ "No"
#         __ ?|? __ ?
#             print("The item was found at index" ?
#             r_ ?
#         # If the item is not equal to the target item,
#         # check if it's larger or smaller and reassign
#         # the bounds appropriately.
#         r_ ?|? > ?
#                 print("This middle element is greater than the target item:" ?|? ">" ?
#                 print("We need to discard the upper half of the list")
#                 print("The lower bound remains at:" ?
#                 print("Now the new upper bound is:" ? - 1)
#                 h.. _ ? - 1
#         ____
#                 print("This middle item is smaller than the target item:" ?|? "<" ?
#                 print("We need to discard the lower half of the list")
#                 print("Now the new lower bound is:" ? + 1)
#                 print("The upper bound remains at:" ?
#                 l.. _ ? + 1
#         i +_ 1
#
#     # Else, if the item is not found in the list, return -1
#     print("The target item was not found in the list")
#     r_ -1
