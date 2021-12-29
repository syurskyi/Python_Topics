"""
Given an array of integers, find if the array contains any duplicates. Your
function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

class Solution(object):
    ___ containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set()
        ___ i __ nums:
            __ i __ d:
                r.. True
            ____:
                d.add(i)
        r.. False
