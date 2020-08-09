"""
Given an array and a value, remove all instances of that value in place and
return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.
"""

class Solution(object
    ___ removeElement(self, nums, val
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = le.(nums)
        j = 0
        ___ i in range(n
            __ nums[i] != val:
                nums[j] = nums[i]
                j += 1
        r_ j
