"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
run time complexity should be O(log (m+n)).
"""
__author__ = 'Danyang'


c_ Solution:
    ___ findMedianSortedArrays(self, A, B):
        """
        Merge two arrays to get the median, O((m+n)/2)

        Algorithm: Find k-th element in 2 array

        A: A_left A[m/2] A_right
        B: B_left B[n/2] A_right
        if A[m/2]>B[n/2] and k>m/2+n/2, then disregard B_left and B[n/2]
        if A[m/2]>B[n/2] and k<=m/2+n/2, then disregard A_right and A[m/2]
        if A[m/2]<=B[n/2] and k>m/2+n/2, then disregard A_left and A[m/2]
        if A[m/2]<=B[n/2] and k<=m/2+n/2, then disregard B_right and B[n/2]

        whether to disregard A[m/2] or B[n/2] takes time to consider
        
        T(N) = T(3/4 N) + O(1), thus T(N) = O(lg N) where N = |A|+|B|
        O(log (m+n)), thus binary search.

        :param A: list
        :param B: list
        :return: float
        """
        m = l..(A)
        n = l..(B)
        __ ((m+n)&1 __ 0):
            r.. (find_kth(A, B, (m+n)/2)+find_kth(A, B, (m+n)/2-1))/2.0
        ____:
            r.. find_kth(A, B, (m+n)/2)

    ___ find_kth(self, A, B, k):
        """

        :param A:
        :param B:
        :param k: index starting from 0
        :return:
        """
        __ n.. A:  r.. B[k]
        __ n.. B:  r.. A[k]
        __ k __ 0: r.. m..(A[0], B[0])

        m, n = l..(A), l..(B)
        # pay attention to consider the equal sign. Assigning equal sign is an art.
        __ A[m/2] >= B[n/2]:
            __ k > m/2+n/2:
                r.. find_kth(A, B[n/2+1:], k-n/2-1)  # exclude B[n/2] to make progress
            ____:
                r.. find_kth(A[:m/2], B, k)  # exclude A[m/2] to make progress
        ____:
            r.. find_kth(B, A, k)


__ __name__ __ "__main__":
    ... Solution().findMedianSortedArrays([1, 2], [1, 2, 3]) __ 2
    ... Solution().findMedianSortedArrays([1, 2], [3]) __ 2
    ... Solution().findMedianSortedArrays([1], [2, 3]) __ 2
    ... Solution().findMedianSortedArrays([1, 2], [1, 2]) __ 1.5
