# Median of Two Sorted Arrays
# Question: There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Solutions:

class Solution:
    """
    @param A, B: integer arrays.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, int(n / 2 + 1))
        else:
            smaller = self.findKth(A, B, int(n / 2))
            bigger = self.findKth(A, B, int(n / 2 + 1))
            return (smaller + bigger) / 2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        a = A[int(k / 2 - 1)] if len(A) >= int(k / 2) else None
        b = B[int(k / 2 - 1)] if len(B) >= int(k / 2) else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[int(k / 2):], B, k - int(k / 2))
        return self.findKth(A, B[int(k / 2):], k - int(k / 2))


Solution().findMedianSortedArrays([1,2,3,4],[7,8,9,10])