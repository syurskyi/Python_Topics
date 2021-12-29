"""
Rainbow Sort
"""
class Solution:
    """
    @param: A: an integer array
    @param: low: An integer
    @param: high: An integer
    @return:
    """
    ___ partition2(self, A, low, high):
        __ not A:
            return

        left, right = 0, len(A) - 1
        i = 0

        while i < right:
            __ A[i] < low:
                A[left], A[i] = A[i], A[left]
                left += 1
                i += 1
            elif A[i] > high:
                A[right], A[i] = A[i], A[right]
                right -= 1
            else:
                i += 1
