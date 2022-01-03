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
            r.. 0
        res = A[0]
        cur_sum = A[0]
        n = l..(A)
        ___ i __ r..(1, n):
            cur_sum = max(cur_sum + A[i], A[i])
            res = max(res, cur_sum)
        # If negative sum is not allowed, add the following line:
        # if res < 0: return 0
        r.. res
