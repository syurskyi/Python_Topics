"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

c_ Solution:
    # @param A, a list of integers
    # @return an integer
    ___ firstMissingPositive  A):
        n = l..(A)
        i = 0
        w.... i < n:
            j = A[i] - 1
            __ A[i] != i + 1 a.. A[i] >= 1 a.. A[i] <= n a.. A[i] != A[j]:
                A[i], A[j] = A[j], A[i]
            ____:
                i += 1
        ___ i, e __ e..(A):
            __ e != i + 1:
                r.. i + 1
        r.. n + 1
