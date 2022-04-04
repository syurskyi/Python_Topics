"""
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""

c_ Solution(o..
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        m = l..(nums) / 2
        d    # dict
        ___ k __ nums:
            __ k n.. __ d:
                d[k] = 1
            ____
                d[k] += 1
        ___ k __ d:
            __ d[k] > m:
                r.. k
