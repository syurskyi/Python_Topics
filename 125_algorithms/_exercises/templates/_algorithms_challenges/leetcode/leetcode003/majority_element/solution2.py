"""
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""

c_ Solution(o..):
    ___ majorityElement  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cand = N..
        ___ c __ nums:
            __ count __ 0:
                cand = c
                count += 1
            ____ cand __ c:
                count += 1
            ____:
                count -= 1
        r.. cand
