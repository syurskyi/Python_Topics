"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose
of space complexity analysis.)
"""
__author__ = 'Daniel'


class Solution:
    ___ productExceptSelf(self, nums):
        """
        dp

        :type nums: list[int]
        :rtype: list[int]
        """
        n = l..(nums)
        left = [1 ___ _ __ xrange(n+1)]  # the 0th one is dummy
        right = [1 ___ _ __ xrange(n+1)]  # the last one is dummy
        ___ i __ xrange(1, n+1):
            left[i] = left[i-1]*nums[i-1]
        ___ i __ xrange(n-1, -1, -1):
            right[i] = right[i+1]*nums[i]

        r.. [left[i]*right[i+1] ___ i __ xrange(n)]