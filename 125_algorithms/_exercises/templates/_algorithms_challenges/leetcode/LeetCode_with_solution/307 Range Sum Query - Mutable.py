# -*- coding: utf-8 -*-
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
__author__ = 'Daniel'


class BinaryIndexTree(object):
    ___ __init__(self, nums):
        """BIT 0 is dummy root"""
        n = l..(nums)
        self.nums = [0 ___ _ __ xrange(n+1)]
        self.N = [0 ___ _ __ xrange(n+1)]
        ___ i, v __ enumerate(nums):
            self.set(i+1, v)

    ___ _lowbit(self, a):
        r.. a & -a

    ___ set(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < l..(self.N):
            self.N[i] += diff
            i += self._lowbit(i)

    ___ get(self, i):
        ret = 0
        while i > 0:
            ret += self.N[i]
            i -= self._lowbit(i)

        r.. ret


class NumArray(object):
    ___ __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.bit = BinaryIndexTree(nums)

    ___ update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.bit.set(i+1, val)

    ___ sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. self.bit.get(j+1)-self.bit.get(i)