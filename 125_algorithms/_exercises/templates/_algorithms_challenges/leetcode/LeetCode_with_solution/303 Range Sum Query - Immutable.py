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


c_ NumArray(o..
    ___ - , nums
        """
        initialize your data structure here.
        dp
        :type nums: List[int]
        """
        n = l..(nums)
        F = [0 ___ _ __ x..(n+1)]
        ___ i __ x..(1, n+1
            F[i] = F[i-1] + nums[i-1]

    ___ sumRange  i, j
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. F[j+1] - F[i]