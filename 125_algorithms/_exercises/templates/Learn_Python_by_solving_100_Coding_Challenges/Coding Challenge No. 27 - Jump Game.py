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
    def canJump(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step > 0:
                step -= 1
                step = max(step, A[i])
        else:
            return False
        return True


Solution().canJump([3,2,1,0,4])