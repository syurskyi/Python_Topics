"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

c_ Solution:
    # @param A, a list of integers
    # @return an integer
    ___ maxSubArray(self, A):
        __ n.. A:
            msg = 'The input array must contain at least one number.'
            raise Exception(msg)
        max_sum = A[0]
        max_current = max_sum
        ___ i __ r..(1, l..(A)):
            max_current = max(A[i], max_current + A[i])
            max_sum = max(max_sum, max_current)
        r.. max_sum
