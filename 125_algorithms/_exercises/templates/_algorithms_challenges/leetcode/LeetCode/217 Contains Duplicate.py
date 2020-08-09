"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.
"""
__author__ = 'Daniel'
from collections ______ Counter


class Solution:
    ___ containsDuplicate(self, nums
        """
        Trival
        :type nums: list[int]
        :rtype : bool
        """
        d = Counter(nums)
        ___ k, v in d.items(
            __ v > 1:
                r_ True

        r_ False
