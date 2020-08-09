'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object
    ___ combinationSum2(self, candidates, target
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        __ not candidates: r_[]
        candidates.sort()
        res = []
        self.helper2(candidates, 0, [], res, target)
        r_ res
    
    ___ helper2(self, nums, ind, curr, res, target
        __ target __ 0:
            res.append(list(curr))
            r_
        for i in range(ind, le.(nums)):
            __ target < nums[i]:
                r_
            __ i > ind and nums[i] __ nums[i-1]:
                continue
            curr.append(nums[i])
            self.helper2(nums, i+1, curr, res, target-nums[i])
            curr.pop()
    
    ___ combinationSum2_origin(self, candidates, target
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        __ not candidates: r_ []
        candidates.sort()
        res = []
        self.helper(candidates, target, 0, [], res)
        r_ res
    
    ___ helper(self, nums, target, ind, curr, res
        __ target __ 0:
            res.append(list(curr))
            r_
        prev = -1
        for i in range(ind, le.(nums)):
            __ nums[i] > target:
                r_
            __ prev != nums[i]:
                curr.append(nums[i])
                self.helper(nums, target-nums[i], i+1, curr, res)
                prev = curr.pop()
