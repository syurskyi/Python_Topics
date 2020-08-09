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
    ___ partition2(self, A, low, high
        __ not A:
            r_

        left, right = 0, le.(A) - 1
        i = 0

        w___ i < right:
            __ A[i] < low:
                A[left], A[i] = A[i], A[left]
                left += 1
                i += 1
            ____ A[i] > high:
                A[right], A[i] = A[i], A[right]
                right -= 1
            ____
                i += 1
