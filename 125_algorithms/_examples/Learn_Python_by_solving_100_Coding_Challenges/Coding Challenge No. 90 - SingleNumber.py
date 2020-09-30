# Single Number
# Question: Given an array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Solutions:


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result


Solution().singleNumber([1, 2, 1, 2, 0])