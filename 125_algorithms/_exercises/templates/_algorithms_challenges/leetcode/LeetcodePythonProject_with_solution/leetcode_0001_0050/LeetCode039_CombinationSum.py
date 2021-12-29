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
        res = []
        self.helper(candidates, 0, [], target, res)
        return res
    
    ___ helper(self, nums, ind, curr, target, res):
        __ target == 0:
            res.append(list(curr))
            return
        __ target < 0:
            return
        for i in range(ind, len(nums)):
            curr.append(nums[i])
            self.helper(nums, i, curr, target-nums[i], res)
            curr.pop()
