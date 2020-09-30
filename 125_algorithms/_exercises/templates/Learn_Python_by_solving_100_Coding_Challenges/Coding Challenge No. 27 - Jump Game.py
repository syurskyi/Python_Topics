# Jump Game
# Question: Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.
# Solutions:


class Solution:
    # @param A, a list of integers
    # @return a boolean
    ___ canJump(self, A):
        step = A[0]
        ___ i __ ra..(1, len(A)):
            if step > 0:
                step -= 1
                step = ma.(step, A[i])
        else:
            r_ False
        r_ True


Solution().canJump([3,2,1,0,4])