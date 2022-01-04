'''
Created on May 31, 2018

@author: tongq
'''
c_ Solution(object):
    ___ subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.s..()
        res    # list
        helper(nums, 0, [], res)
        r.. res
    
    ___ helper(self, nums, ind, curr, res):
        res.a..(l..(curr))
        ___ i __ r..(ind, l..(nums)):
            __ i > ind a.. nums[i] __ nums[i-1]:
                _____
            curr.a..(nums[i])
            helper(nums, i+1, curr, res)
            curr.pop()
