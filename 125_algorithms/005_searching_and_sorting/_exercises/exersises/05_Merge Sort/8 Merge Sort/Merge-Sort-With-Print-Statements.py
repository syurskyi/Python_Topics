# ___ merge_sort lst
#
#     print("\n======> Calling merge_sort()")
#
#     print("List:" ?
#     print("List length:" le. ?
#
#     __ le. ? __ 0 o. le. ? __ 1
#         print("The list is empty or it only contains one item")
#         print("Returning list:" ?
#         r_ ?
#     ____
#         middle_index _ le. ?//2
#         print("Middle index:" ?
#         print("Left half:" ?|;?
#         print("Right half:" ?|?;
#
#         print("Calling merge_sort() for the left half:" ?|;?
#         left _ ? ?|;?
#         print("Calling merge_sort() for the right half:" ?|?;
#         right _ ? ?|?;
#
#         # Small adjustments to the original implementation
#         # for the print statements
#         print("Merging the two halves...")
#         final_list _ ? ? ?
#
#         print("\nBack to merge_sort()")
#         print("Resulting merged list:" ?
#
#         r_ ?
#
#
# ___ merge left_half right_half
#
#     print("\n---> Inside merge()")
#
#     print("Merging...")
#     print("Left half" ?
#     print("Right half" ?
#
#     __ no. ? o. no. ?
#         print("One of the lists is empty")
#         print("Returning" ? o. ?)
#         r_ ? o. ?
#
#     result _    # list
#     i, j _ 0, 0
#
#     print("\n-> While loop")
#     w___ T..
#         print("i _" ?
#         print("j _" ?
#
#         print _*\nIs the element left_half|? ||?|? < the element right_half|? ||?|j
#         __ ?|? < ?|?
#             print("Yes,it is!")
#             print _*Append the element left_half|? ||?|? to the list 'result'
#             print("List 'r..' before:" ?
#             ?.ap..(l..|?
#             print("List 'r..' after:" ?
#             i +_ 1
#             print("We've assigned one element of the left half")
#             print("Incrementing the value of i to:" ?
#
#         ____
#             print("No, it isn't!")
#             print _*Appending right_half|? ||?|? to the list 'result'
#             print("List 'r..' before:" ?
#             ?.ap.. ?|?
#             print("List 'result' after:" ?
#             ? +_ 1
#             print("We've assigned one element of the right half")
#             print("Incrementing the value of j to:" ?
#
#         print("\nHave we reached the end of either one of the lists?", "Yes" __ ? __ le. ? o. ? __ le. ? ____ "No")
#         __ i __ le. ? o. j __ le. ?
#             print("We reached the end of", "the left half" __ ? __ le. ? ____ "the right half")
#             print("Extending the list 'result' with the remaining item(s):" ?|?; o. ?|?;
#             ?.ex.. ?|?; o. ?|?;
#             b..
#         ____
#             print("Let's continue the while loop")
#
#     print("Returning the list 'r..':" ?
#     r_ ?
