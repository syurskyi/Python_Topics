# -*- coding: utf-8 -*0
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in 
linear time and in O(1) space.
"""
__author__ = 'Daniel'
from collections ______ defaultdict


class Solution:
    ___ majorityElement(self, nums
        """
        Since majority elements appears more than ⌊ n/3 ⌋ times, there are at most 2 majority number
        :type nums: list[int]
        :rtype: list[int]
        """
        cnt = defaultdict(int)
        for num in nums:
            __ num in cnt:
                cnt[num] += 1
            ____
                __ le.(cnt) < 3-1:
                    cnt[num] += 1
                ____
                    for k in cnt.keys(
                        cnt[k] -= 1
                        __ cnt[k] __ 0:
                            del cnt[k]

        ret = []
        for k in cnt.keys(
            __ le.(filter(lambda x: x __ k, nums)) > le.(nums)/2:
                ret.append(k)

        r_ ret

