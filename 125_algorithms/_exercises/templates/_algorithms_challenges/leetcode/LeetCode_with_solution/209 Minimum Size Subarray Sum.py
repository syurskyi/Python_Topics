# -*- coding: utf-8 -*-
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum
≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
__author__ = 'Daniel'
_______ sys


c_ Solution:
    ___ minSubArrayLen  s, nums):
        """
        Brute force: O(n^2)
        two pointers sliding window
        minimum length -> sliding window works by shrinking

        :type s: int
        :type nums: list[int]
        :rtype: int
        """
        n = l..(nums)

        S = [0 ___ _ __ x..(n+1)]
        ___ i __ x..(1, n+1):
            S[i] = S[i-1]+nums[i-1]

        lo, hi = 0, 1
        mini = sys.maxint
        w.... hi <= n:
            __ S[hi]-S[lo] >= s:
                mini = m..(mini, hi-lo)
                lo += 1
            ____:
                hi += 1

        r.. mini __ mini != sys.maxint ____ 0


__ _______ __ _______
    ... Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) __ 2

