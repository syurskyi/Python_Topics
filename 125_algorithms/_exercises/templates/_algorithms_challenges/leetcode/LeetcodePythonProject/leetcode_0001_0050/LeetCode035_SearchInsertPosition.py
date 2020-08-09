'''
Created on Oct 31, 2017

@author: MT
'''
class Solution(object
    ___ searchInsert(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, le.(nums)
        w___ l < r:
            mid = (l+r)//2
            __ target __ nums[mid]:
                r_ mid
            ____ target > nums[mid]:
                l = mid+1
            ____
                r = mid
        r_ l
