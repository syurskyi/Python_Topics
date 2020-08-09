"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""
__author__ = 'Daniel'


class NumArray(object
    ___ __init__(self, nums
        """
        initialize your data structure here.
        dp
        :type nums: List[int]
        """
        n = le.(nums)
        self.F = [0 ___ _ in xrange(n+1)]
        ___ i in xrange(1, n+1
            self.F[i] = self.F[i-1] + nums[i-1]

    ___ sumRange(self, i, j
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        r_ self.F[j+1] - self.F[i]