# """
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
# run time complexity should be O(log (m+n)).
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ findMedianSortedArrays  A B
#         """
#         Merge two arrays to get the median, O((m+n)/2)
#
#         Algorithm: Find k-th element in 2 array
#
#         A: A_left A[m/2] A_right
#         B: B_left B[n/2] A_right
#         if A[m/2]>B[n/2] and k>m/2+n/2, then disregard B_left and B[n/2]
#         if A[m/2]>B[n/2] and k<=m/2+n/2, then disregard A_right and A[m/2]
#         if A[m/2]<=B[n/2] and k>m/2+n/2, then disregard A_left and A[m/2]
#         if A[m/2]<=B[n/2] and k<=m/2+n/2, then disregard B_right and B[n/2]
#
#         whether to disregard A[m/2] or B[n/2] takes time to consider
#
#         T(N) = T(3/4 N) + O(1), thus T(N) = O(lg N) where N = |A|+|B|
#         O(log (m+n)), thus binary search.
#
#         :param A: list
#         :param B: list
#         :return: float
#         """
#         m  l.. A
#         n  l.. B
#         __ ?+? &1 __ 0)
#             r..  ? ? ? ?+?/2 + ? ? ? ?+?/2-1))/2.0
#         ____:
#             r.. ? ? ? ?+?/2
#
#     ___ find_kth  A B k
#         """
#
#         :param A:
#         :param B:
#         :param k: index starting from 0
#         :return:
#         """
#         __ n.. A  r.. ? ?
#         __ n.. B  r.. ? ?
#         __ k __ 0 r.. m.. ? 0 ? 0
#
#         m, n =l.. ? l.. ?
#         # pay attention to consider the equal sign. Assigning equal sign is an art.
#         __ ? ?/2 >_ ? ?/2
#             __ k > ?/2+?/2:
#                 r.. ? ? ? ?/2+1| ?-?/2-1  # exclude B[n/2] to make progress
#             ____:
#                 r.. ? ? |?/2] ? ?  # exclude A[m/2] to make progress
#         ____:
#             r.. ? ? ? ?
#
#
# __ _______ __ _______
#     ... ?.f.. 1, 2], [1, 2, 3]) __ 2
#     ... ?.f.. 1, 2], [3]) __ 2
#     ... ?.f.. 1], [2, 3]) __ 2
#     ... ?.f.. 1, 2], [1, 2]) __ 1.5
