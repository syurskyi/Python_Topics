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
        for i in nums:
            __ i in d:
                return True
            else:
                d.add(i)
        return False
