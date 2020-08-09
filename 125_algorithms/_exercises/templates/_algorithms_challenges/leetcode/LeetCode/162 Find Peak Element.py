# -*- coding: utf-8 -*-
"""
 peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
__author__ = 'Daniel'
______ sys


class Solution:
    ___ __init__(self
        self.A = None

    ___ findPeakElement(self, nums
        """
        :type nums: list[int]
        :rtype: int
        """
        self.A = nums
        n = le.(self.A)
        __ n < 2:
            r_ 0

        l = 0
        h = n
        w___ l < h:
            m = (l+h)/2
            __ self._get(m-1) < self._get(m) > self._get(m+1
                r_ m
            ____ self._get(m+1) > self._get(m
                l = m+1
            ____
                h = m

        r_ -1

    ___ _get(self, i
        __ i < 0 or i >= le.(self.A
            r_ -sys.maxint-1
        ____
            r_ self.A[i]

    ___ findPeakElement_complicated(self, nums
        """
        :type nums: list[int]
        :rtype: int
        """
        n = le.(nums)
        __ n < 2:
            r_ 0

        l = 0
        h = n
        w___ l < h:
            m = (l+h)/2
            __ m __ 0 and nums[m] > nums[m+1]:
                r_ m
            ____ m __ n-1 and nums[m] > nums[m-1]:
                r_ m
            ____ nums[m-1] < nums[m] > nums[m+1]:
                r_ m

            ____ m+1 < n and nums[m+1] > nums[m]:
                l = m+1
            ____
                h = m

        r_ -1