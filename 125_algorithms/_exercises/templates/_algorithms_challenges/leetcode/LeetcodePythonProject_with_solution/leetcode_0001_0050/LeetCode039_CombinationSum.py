'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    ___ combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res    # list
        self.helper(candidates, 0, [], target, res)
        r.. res
    
    ___ helper(self, nums, ind, curr, target, res):
        __ target __ 0:
            res.a..(l..(curr))
            r..
        __ target < 0:
            r..
        ___ i __ r..(ind, l..(nums)):
            curr.a..(nums[i])
            self.helper(nums, i, curr, target-nums[i], res)
            curr.pop()
