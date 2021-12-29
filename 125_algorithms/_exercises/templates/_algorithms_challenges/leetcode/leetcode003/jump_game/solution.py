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
        t = 0  # Number of remaining steps
        ___ i __ r..(1, n):
            # t is max number of steps that remained if reaching A[i]
            t = max(t, A[i - 1]) - 1
            __ t < 0:
                r.. False
        r.. True
