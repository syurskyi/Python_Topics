# # Merge Sorted Array
# # Question: Given two sorted integer arrays A and B, merge B into A as one sorted array.
# # Note: You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
# # Solutions:
#
#
# c_ Solution object
#     ___ merge  A m B n
#         """
#         :type A: List[int]
#         :type m: int
#         :type B: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify A in-place instead.
#         """
#         indexA _ ? - 1
#         indexB _ ? - 1
#         w___ ? >_0 an. ? >_ 0
#             __ ? ? > ? ?
#                 ? ? + ? + 1 _ ? ?
#                 ? -_ 1
#             ____
#                 ? ? + ? + 1 _ ? ?
#                 ? -_ 1
#         w___ ? >_ 0
#             ? ? _ ? ?
#             ? -_ 1
#
# ?.? [1],1,  # list,0)
#
# # All you need is understanding the algorithm, don't try other cases.
# # In case you're wondering, if the requirements do not include modifying an array in-place. This is how you merge arrays:
#
# arr1 _ [1,2,3,10,20]
# arr2 _ [2,2,10,60]
# result _ s.. ? + ?
# print ?