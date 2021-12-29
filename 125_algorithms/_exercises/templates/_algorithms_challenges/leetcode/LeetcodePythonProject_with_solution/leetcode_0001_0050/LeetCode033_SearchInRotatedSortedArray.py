'''
Created on Oct 31, 2017

@author: MT
'''
class Solution(object):
    ___ search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            __ nums[mid] == target:
                return mid
            __ nums[l] <= nums[mid]:
                __ nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                __ nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
