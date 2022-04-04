# -*- coding: utf-8 -*-
"""
 peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
__author__ = 'Daniel'
_______ ___


c_ Solution:
    ___ -
        A = N..

    ___ findPeakElement  nums
        """
        :type nums: list[int]
        :rtype: int
        """
        A = nums
        n = l..(A)
        __ n < 2:
            r.. 0

        l = 0
        h = n
        w.... l < h:
            m = (l+h)/2
            __ _get(m-1) < _get(m) > _get(m+1
                r.. m
            ____ _get(m+1) > _get(m
                l = m+1
            ____
                h = m

        r.. -1

    ___ _get  i
        __ i < 0 o. i >_ l..(A
            r.. -___.maxint-1
        ____
            r.. A[i]

    ___ findPeakElement_complicated  nums
        """
        :type nums: list[int]
        :rtype: int
        """
        n = l..(nums)
        __ n < 2:
            r.. 0

        l = 0
        h = n
        w.... l < h:
            m = (l+h)/2
            __ m __ 0 a.. nums[m] > nums[m+1]:
                r.. m
            ____ m __ n-1 a.. nums[m] > nums[m-1]:
                r.. m
            ____ nums[m-1] < nums[m] > nums[m+1]:
                r.. m

            ____ m+1 < n a.. nums[m+1] > nums[m]:
                l = m+1
            ____
                h = m

        r.. -1