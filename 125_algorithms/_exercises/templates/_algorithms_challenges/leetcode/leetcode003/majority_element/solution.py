"""
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""

class Solution(object
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        m = le.(nums) / 2
        d = {}
        ___ k in nums:
            __ k not in d:
                d[k] = 1
            ____
                d[k] += 1
        ___ k in d:
            __ d[k] > m:
                r_ k
