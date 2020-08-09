'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object
    ___ combinationSum(self, candidates, target
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, 0, [], target, res)
        r_ res
    
    ___ helper(self, nums, ind, curr, target, res
        __ target __ 0:
            res.append(list(curr))
            r_
        __ target < 0:
            r_
        for i in range(ind, le.(nums)):
            curr.append(nums[i])
            self.helper(nums, i, curr, target-nums[i], res)
            curr.pop()
