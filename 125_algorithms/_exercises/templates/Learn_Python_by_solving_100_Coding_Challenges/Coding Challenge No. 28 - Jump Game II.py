# Jump Game II
# Question: Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.
# For example:
# Given array A = [2,3,1,1,4]
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
# Solutions:


class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ jump(self, A):
        p = [0]
        ___ i __ ra..(len(A) - 1):
            while(i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)
        r_ p[-1]


Solution().jump([2,3,1,1,4])