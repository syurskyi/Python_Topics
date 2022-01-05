"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-
zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

__author__ = 'Daniel'


c_ Solution(o..):
    ___ moveZeroes  nums):
        """
        Two pointers at the left side
        Pivot
        """
        left = -1
        ___ i __ x..(l..(nums)):
            __ nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]


c_ SolutionCount(o..):
    ___ moveZeroes  nums):
        """
        In-place
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        ___ elt __ nums:
            __ elt != 0:
                nums[cnt] = elt
                cnt += 1

        ___ j __ x..(cnt, l..(nums)):
            nums[j] = 0


__ _______ __ _______
    lst = [0, 1, 0, 3, 12]
    Solution().moveZeroes(lst)
    ... lst __ [1, 3, 12, 0, 0]
