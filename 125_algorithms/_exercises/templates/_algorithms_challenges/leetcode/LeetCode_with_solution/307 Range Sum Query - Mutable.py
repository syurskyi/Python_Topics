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


c_ BinaryIndexTree(object):
    ___ - , nums):
        """BIT 0 is dummy root"""
        n = l..(nums)
        nums = [0 ___ _ __ xrange(n+1)]
        N = [0 ___ _ __ xrange(n+1)]
        ___ i, v __ e..(nums):
            set(i+1, v)

    ___ _lowbit(self, a):
        r.. a & -a

    ___ set(self, i, val):
        diff = val - nums[i]
        nums[i] = val
        w.... i < l..(N):
            N[i] += diff
            i += _lowbit(i)

    ___ get(self, i):
        ret = 0
        w.... i > 0:
            ret += N[i]
            i -= _lowbit(i)

        r.. ret


c_ NumArray(object):
    ___ - , nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        bit = BinaryIndexTree(nums)

    ___ update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        bit.set(i+1, val)

    ___ sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. bit.get(j+1)-bit.get(i)