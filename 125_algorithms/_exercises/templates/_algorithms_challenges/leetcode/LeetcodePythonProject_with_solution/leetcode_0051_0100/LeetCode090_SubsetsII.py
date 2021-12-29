'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object):
    ___ subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res    # list
        self.helper(nums, 0, [], res)
        r.. res
    
    ___ helper(self, nums, ind, curr, res):
        res.a..(l..(curr))
        ___ i __ r..(ind, l..(nums)):
            __ i > ind and nums[i] __ nums[i-1]:
                continue
            curr.a..(nums[i])
            self.helper(nums, i+1, curr, res)
            curr.pop()
