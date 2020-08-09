"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ firstMissingPositive(self, A
        n = le.(A)
        i = 0
        w___ i < n:
            j = A[i] - 1
            __ A[i] != i + 1 and A[i] >= 1 and A[i] <= n and A[i] != A[j]:
                A[i], A[j] = A[j], A[i]
            ____
                i += 1
        for i, e in enumerate(A
            __ e != i + 1:
                r_ i + 1
        r_ n + 1
