'''
Created on Oct 31, 2017

@author: MT
'''
c_ Solution(o..
    ___ s..  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, l..(nums)-1
        w.... l <= r:
            mid = (l+r)//2
            __ nums[mid] __ target:
                r.. mid
            __ nums[l] <= nums[mid]:
                __ nums[l] <= target < nums[mid]:
                    r = mid-1
                ____:
                    l = mid+1
            ____:
                __ nums[mid] <= target <= nums[r]:
                    l = mid+1
                ____:
                    r = mid-1
        r.. -1
