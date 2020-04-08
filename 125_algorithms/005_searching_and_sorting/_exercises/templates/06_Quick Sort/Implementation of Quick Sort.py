# # Implementation of Quick Sort
# # A quick sort first selects a value, which is called the pivot value. Although there are many different ways to choose
# # the pivot value, we will simply use the first item in the list. The role of the pivot value is to assist with
# # splitting the list. The actual position where the pivot value belongs in the final sorted list, commonly called
# # the split point, will be used to divide the list for subsequent calls to the quick sort.
# # Resources for Review
# # Check out the resources below for a review of Insertion sort!
# #     Wikipedia
# #     Visual Algo
# #     Sorting Algorithms Animcation with Pseudocode
#
# ___ quick_sort arr
#
#     ?h ? 0 le. ? - 1
#
# ___ quick_sort_help arr first last
#
#     __ ? < ?
#
#
#         splitpoint _ ? ? ? ?
#
#         ? ? ? ? - 1
#         ? ? ? + 1 ?
#
#
# ___ partition arr first last
#
#     pivotvalue _ ?|?
#
#     leftmark _ ?+1
#     rightmark _ ?
#
#     done _ F..
#     w___ not done:
#
#         w___ ? <_ ? an. ?|l.. <_ ?
#             ? _ ? + 1
#
#         w___ ?|? >_ p.. an. ? >_ ?
#             ? _ ? -1
#
#         __ ? < ?
#             d.. _ T..
#         ____
#             temp _ ?|l..
#             ?|l.. _ ?|?
#             ?|? _ ?
#
#     temp _ ?|f..
#     ?|f.. _ ?|?
#     ?|r.. _ ?
#
#
#     r_ ?
#
# arr _ [2,5,4,6,7,3,1,4,12,11]
# ? ?
# ?
# # [1, 2, 3, 4, 4, 5, 6, 7, 11, 12]
# #
# # Good Job!