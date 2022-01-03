# -*- coding: utf-8 -*-
"""
Given an integer array of size n, find all elements that appear more than ⌊
n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
"""

c_ Solution(object):
    ___ majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1 = N..
        cand2 = N..
        count1 = 0
        count2 = 0
        ___ c __ nums:
            __ cand1 __ c:
                count1 += 1
            ____ cand2 __ c:
                count2 += 1
            ____ count1 __ 0:
                cand1 = c
                count1 += 1
            ____ count2 __ 0:
                cand2 = c
                count2 += 1
            ____:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        ___ c __ nums:
            __ cand1 __ c:
                count1 += 1
            ____ cand2 __ c:
                count2 += 1
        m = l..(nums) / 3
        res    # list
        __ count1 > m:
            res.a..(cand1)
        __ count2 > m:
            res.a..(cand2)
        r.. res


a1 = [8, 8, 7, 7, 7]
a2 = [1, 2]
s = Solution()
print s.majorityElement(a1)
print s.majorityElement(a2)
