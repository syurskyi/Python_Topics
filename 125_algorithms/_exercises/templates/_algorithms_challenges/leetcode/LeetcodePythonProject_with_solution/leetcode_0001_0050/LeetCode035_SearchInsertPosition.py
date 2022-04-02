'''
Created on Oct 31, 2017

@author: MT
'''
c_ Solution(o..
    ___ searchInsert  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, l..(nums)
        w.... l < r:
            mid = (l+r)//2
            __ target __ nums[mid]:
                r.. mid
            ____ target > nums[mid]:
                l = mid+1
            ____:
                r = mid
        r.. l
