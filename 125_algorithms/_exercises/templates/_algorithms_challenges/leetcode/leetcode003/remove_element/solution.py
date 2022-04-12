"""
Given an array and a value, remove all instances of that value in place and
return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.
"""

c_ Solution(o..
    ___ removeElement  nums, val
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n l..(nums)
        j 0
        ___ i __ r..(n
            __ nums[i] !_ val:
                nums[j] nums[i]
                j += 1
        r.. j
