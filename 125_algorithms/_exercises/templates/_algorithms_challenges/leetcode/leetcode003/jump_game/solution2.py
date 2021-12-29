"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that
position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    ___ canJump(self, A):
        n = l..(A)
        __ n __ 1:
            r.. True
        # d[i] is the max index A[i] can reach in A
        d = [i + A[i] ___ i __ r..(n)]
        reach = n - 1
        ___ i __ r..(1, n):
            # j is from n - 1 to 0
            j = n - 1 - i
            __ d[j] >= reach:
                reach = j
        r.. reach __ 0
