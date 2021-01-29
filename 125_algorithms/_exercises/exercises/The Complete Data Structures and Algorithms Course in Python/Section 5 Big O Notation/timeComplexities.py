# #  Created by Elshad Karimov on 3/17/20.
# #  Copyright © 2020 Elshad Karimov. All rights reserved.
#
#
# array = [1, 2, 3, 4, 5]
#
# ######  Constant time complexity  #######
# print('######  Constant time complexity  #######')
# print(? 0
#
#
# ######  Linear time complexity  #######
# print('######  Linear time complexity  #######')
# ___ element __ ?
#      print ?
#
#
# ######  Logarithmic time complexity  #######
# print('######  Logarithmic time complexity  #######')
# ___ index __ ra__ 0 le_ ? 3
#      print ? ?
#
#
# ######  Quadratic time complexity  #######
# print('######  Quadratic time complexity  #######')
# ___ x __ ?
#     ___ y __ ?
#          print ?
#
#
# ######  Exponential time complexity  #######
# print('######  Exponential time complexity  #######')
# ___ fibonacci n
#     __ ? <_ 1
#         r_ ?
#     r_ ? ? - 1 + ? ? - 2
#
#
# ######  Add vs Multiply #######
# arrayA = [1,2,3,4,5,6,7,8,9]
# arrayB = [11,12,13,14,15,16,17,18,19]
#
# ___ a __ ?
#     print ?
#
# ___ b __ ?
#     print ?
#
# ___ a __ ?
#     ___ b __ ?
#         print ? ?
#
# ######  Iterative algorithm - finding the biggest number in the array #######
#
# sample1Array _ [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]
#
# ___ findBiggestNumber sampleArray
#     biggestNumber _ ? 0
#     ___ index __ ra__ 1 le_ ?
#         __ ? ? > b..
#             b.. _ ? ?
#     print ?
#
# findBiggestNumber(sample1Array)
#
# ######  Recursive algorithm - finding the biggest number in the array #######
#
# ___ findMaxNumRec sampleArray n
#     __ ? __ 1
#        r_ ? 0
#     r_ ma_ s.. ? - 1 ? s.. ? - 1
#
# print ? s.. le_ s..
#
#
# ######  Recursive algorithm multiple calls #######
#
# ___ f n
#     __ ? <_ 1
#         r_ 1
#     r_ ? ? - 1 + ? ? - 1
#
# print(f(3))
#
#
#
#
#
#
#
# ######  Quiz Questions #######
#
#
# ___ f1 n
#     __ ? <_ 0
#         r_ 1
#     ____
#         r_ 1 + ? ? - 1
#
#
# ___ f2 n
#     __ ? <_ 0
#         r_ 1
#     ____
#         r_ 1 + ? ? - 5
#
#
# ___ f3 n
#     __ ? <_ 0
#         r_ 1
#     ____
#         r_ 1 +? ?/5
#
#
# ___ f4 n m o
#     __ ?<_0
#         print ? ? ?
#     ____
#         ? ?-1 ?+1 ?
#         ? ?-1 ? ?+1
#
# ___ f5 n
#     ___ i __ ra__ 0 ? 2
#         print ?
#     __ ?<_0
#         r_ 1
#     ____
#         r_ 1 + ? ? - 5
#
