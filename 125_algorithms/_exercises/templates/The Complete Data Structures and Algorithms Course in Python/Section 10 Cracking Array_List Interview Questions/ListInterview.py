# #   Created by Elshad Karimov on 15/04/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# #  Question 1
#
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#
#
# ___ findMissing li__ n
#     sum1 = su_ li__
#     sum2 = 100*101/2
#     print ? - ?
#
#
# # findMissing(mylist, 100)
#
# # Question 2
# ___ findPairs li__ su_
#     ___ i __ ra__ le_ li__
#         ___ j __ ra__ ? + 1 le_ li__
#             __ (li__ ? + li__ ? __ su_
#                 print(li__? li__ ?
# # findPairs(mylist, 100)
#
#
# # Question 3
# import numpy as np
# myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#
# ___ findNumber array number
#     ___ i __ ra__ le_ ?
#         __ ? ? __ ?
#             print ?
#
# findNumber(myArray, 12)
#
# # Question 3
#
# ___ findMaxProduct array
#     maxProduct _ 0
#     ___ i __ ra__ le_ ?
#         ___ j __ ra__ ? + 1 le_ ?
#             __ ? ? * ? ? > m..
#                 m.. _ ? ? * ? ?
#                 pairs _ st. ? ? + "," + st. ? ?
#     print(p..
#     print m..
#
# findMaxProduct(myArray)
#
#
#
# #Question 5 - isqunieuq
# ___ isUnique li__
#   a # list
#   ___ i __ li__
#     __ i __ a
#         print
#         r_ F..
#     ____
#         a.ap.. ?
#   r_ T..
#
# print(isUnique(myList))
#
#
#
# #Question 6 - permutation
#
# ___ permuntation list1, list2
#     print ?
#     print ?.re__
#     __ ? __ ?   # if list1 == list2.reverse() -- false
#         r_ T..
#     ____
#         r_ F..
#
# # print(permuntation([1,2,3], [3,2,1]))
#
#
# # Question 7
#
# ___ rotate_matrix matrix
#     '''rotates a matrix 90 degrees clockwise'''
#     n = le_ ?
#     ___ layer __ ra__ ? // 2
#         first, last _ l.. ? - ? - 1
#         ___ i __ ra__ ? ?
#             # save top
#             top = ? ? ?
#
#             # left -> top
#             ? ? ? _ ? -? - 1||?
#
#             # bottom -> left
#             ? -? - 1||? _ ? -? - 1||-? - 1]
#
#             # right -> bottom
#             ? -? - 1||-? - 1 _ ? ?||- l.. - 1]
#
#             # top -> right
#             ? ?||- l.. - 1] _ t..
#     r_ ?
#
# matrix = [[1,2], [3,4]]
# print(matrix)
# print(rotate_matrix(matrix))