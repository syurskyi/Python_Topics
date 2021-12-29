# # Median of Two Sorted Arrays
# # Question: There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# # Solutions:
#
# c_ Solution
#     """
#     @param A, B: integer arrays.
#     @return: a double whose format is *.5 or *.0
#     """
#     ___ findMedianSortedArrays  A B
#         n _ le. ? + le. ?
#         __ ? % 2 __ 1
#             r_ ? ? ? in. ? / 2 + 1
#         ____
#             smaller _ ? ? ? in. ? / 2
#             bigger _ ? ? ? in. ? / 2 + 1
#             r_  ? + ? / 2.0
#
#     ___ findKth  A B k
#         __ le. ? __ 0
#             r_ ? ? - 1
#         __ le. ? __ 0
#             r_ ? ? - 1
#         __ ? __ 1
#             r_ mi. ? 0 ? 0
#         a _ ? in. ? / 2 - 1 __ le. ? >_ in. ? / 2 ____ N..
#         b _ ? in. ? / 2 - 1 __ le. ? >_ in. ? / 2 ____ N..
#         __ ? __ N.. o.  ? __ no. N.. an. ? < ?
#             r_ ? ? in. ? / 2| ? ? - in. ? / 2
#         r_ ? ? ? in. ? / 2| ? - in. ? / 2
#
#
# ? .? [1,2,3,4],[7,8,9,10]