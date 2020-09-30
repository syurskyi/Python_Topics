# Median of Two Sorted Arrays
# Question: There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Solutions:

class Solution:
    """
    @param A, B: integer arrays.
    @return: a double whose format is *.5 or *.0
    """
    ___ findMedianSortedArrays(self, A, B):
        n _ le.(A) + le.(B)
        __ n % 2 __ 1:
            r_ self.findKth(A, B, in.(n / 2 + 1))
        ____
            smaller _ self.findKth(A, B, in.(n / 2))
            bigger _ self.findKth(A, B, in.(n / 2 + 1))
            r_ (smaller + bigger) / 2.0

    ___ findKth(self, A, B, k):
        __ le.(A) __ 0:
            r_ B[k - 1]
        __ le.(B) __ 0:
            r_ A[k - 1]
        __ k __ 1:
            r_ min(A[0], B[0])
        a _ A[in.(k / 2 - 1)] __ le.(A) >_ in.(k / 2) ____ None
        b _ B[in.(k / 2 - 1)] __ le.(B) >_ in.(k / 2) ____ None
        __ b is None or (a is not None an. a < b):
            r_ self.findKth(A[in.(k / 2):], B, k - in.(k / 2))
        r_ self.findKth(A, B[in.(k / 2):], k - in.(k / 2))


Solution().findMedianSortedArrays([1,2,3,4],[7,8,9,10])