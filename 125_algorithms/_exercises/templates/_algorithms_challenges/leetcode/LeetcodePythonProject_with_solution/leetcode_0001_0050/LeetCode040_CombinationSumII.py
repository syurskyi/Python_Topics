'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    ___ combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        __ not candidates: return[]
        candidates.sort()
        res = []
        self.helper2(candidates, 0, [], res, target)
        return res
    
    ___ helper2(self, nums, ind, curr, res, target):
        __ target == 0:
            res.append(list(curr))
            return
        for i in range(ind, len(nums)):
            __ target < nums[i]:
                return
            __ i > ind and nums[i] == nums[i-1]:
                continue
            curr.append(nums[i])
            self.helper2(nums, i+1, curr, res, target-nums[i])
            curr.pop()
    
    ___ combinationSum2_origin(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        __ not candidates: return []
        candidates.sort()
        res = []
        self.helper(candidates, target, 0, [], res)
        return res
    
    ___ helper(self, nums, target, ind, curr, res):
        __ target == 0:
            res.append(list(curr))
            return
        prev = -1
        for i in range(ind, len(nums)):
            __ nums[i] > target:
                return
            __ prev != nums[i]:
                curr.append(nums[i])
                self.helper(nums, target-nums[i], i+1, curr, res)
                prev = curr.pop()
