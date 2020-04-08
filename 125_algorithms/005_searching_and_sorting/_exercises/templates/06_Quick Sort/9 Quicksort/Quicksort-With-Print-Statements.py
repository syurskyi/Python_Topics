# ___ quicksort lst low high
#
#     print("\n=======> Starting quicksort()")
#     print("List:" ?
#     print("Low (index):" ?
#     print("High (index):" ?
#
#     print _*Is the interval [|?, |?] valid (has more than 1 element)?", "Yes" __ ? < ? ____ "No
#
#     # If the interval [low, high] is valid
#     __ ? < ?
#
#         # Partition the list and get the partitioning index.
#         pivot_index _ ? ? ? ?
#
#         print("\n-> Back to quicksort()\n")
#         print("The pivot index is:" ?
#
#         # Sort the elements in the list
#         # that come before and after the partition
#
#         print("Calling quicksort() recursively passing:")
#         print("List:" ?
#         print("Low:" ?
#         print("High:" ?-1
#
#         ? ? ? ?-1
#
#         print("\n-> Back to quicksort()\n")
#
#         print("Calling quicksort() recursively passing:")
#         print("List:" ?
#         print("Low:" ?+1
#         print("High:"? ?
#
#         ? ? ?+1 ?
#     ____
#         print("This part of the recursive process stops.")
#
# # Using Lomuto's Partition Scheme
# ___ partition lst low high
#
#     print("\n---> Entering partition()")
#
#     # Pivot
#     pivot _ ?[?]
#
#     print("The p.. is the element:" ?
#     print("Located at index:" ?)
#
#     i _ ? - 1
#
#     print("i is initialized to:" ?
#
#     print("\n-> Starting the For loop")
#
#     ___ j __ ra.. ? ?
#
#         print("\nValue of j:" ?
#         print _*Is the current element ?||? ||?|? <= to the p.. ||?  ?")
#         print("Yes, it is!" __  ?[j] <= pivot else "No, it isn't! We don't need to make any changes")
#
#         # If the current element is smaller than
#         # or equal to pivot
#         __ ?|? <_ p..
#             # Increment index
#             print("\nSo we need to increment the value of i")
#             print("Old value of i:" ?
#             ? +_ 1
#             print("New value of i:", i)
#
#             print _*\nAnd we need to swap the element at index i (index |?):", ?|?
#             print _*with the element at index j (index |?):", ?|?)
#             print("\nSwapping...")
#             print("Old list:" ?)
#             ?|? ?|? _ ?|? ?|?
#             print("New list:" ?)
#             print("Swap completed")
#
#     # Put the pivot where it should be
#     # at index i+1 by swapping it with that element
#     print("\n--> Out of the for loop")
#
#     print _*\nNow we need to move the pivot to index ?+1 (index |?+1)")
#
#     print("\nSwapping...")
#     print _*Swapping the pivot ||?|? with the element at index |?+1 ||?|i+1
#     print("\nOld list:" ?
#     ?|?+1 ?|? _ ?|? ?|?+1
#     print("New list:" ?)
#     print("Swap completed!")
#
#     print _*\nReturning the index of the pivot element after the swap: |?+1}")
#     print("\nThis generates a partition of the list:")
#     print("List:" ?)
#     print("Left sublist:", ?|?;?+1  "where all the elements are smaller than the pivot.")
#     print("Right sublist:", ?|?+2;?+1 "where all the elements are greater than the pivot.")
#     print("The pivot element is in the middle.")
#
#     print("\nPartition Completed!")
#     r_ ?+1
