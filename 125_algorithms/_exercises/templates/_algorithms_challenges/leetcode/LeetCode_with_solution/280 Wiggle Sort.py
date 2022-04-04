"""
Premium Question
nums[0] <= nums[1] >= nums[2] <= nums[3]...
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ wiggleSort  nums
        """
        Solve by enumerating examples
        Sort-based: interleave the small half and large half
        
        Time: O(n lg n)
        Space: O(1)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        ___ elt __ s..(nums
            __ i >_ l..(nums
                i = 1
            nums[i] = elt
            i += 2
