"""
Premium Question
nums[0] <= nums[1] >= nums[2] <= nums[3]...
"""
__author__ = 'Daniel'


class Solution(object
    ___ wiggleSort(self, nums
        """
        Solve by enumerating examples
        Sort-based: interleave the small half and large half
        
        Time: O(n lg n)
        Space: O(1)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        ___ elt __ sorted(nums
            __ i >= le.(nums
                i = 1
            nums[i] = elt
            i += 2
