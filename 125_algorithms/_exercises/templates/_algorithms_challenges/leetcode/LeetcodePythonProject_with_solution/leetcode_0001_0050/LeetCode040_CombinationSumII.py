'''
Created on Jun 6, 2018

@author: tongq
'''
c_ Solution(object):
    ___ combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        __ n.. candidates: r..[]
        candidates.s..()
        res    # list
        helper2(candidates, 0, [], res, target)
        r.. res
    
    ___ helper2(self, nums, ind, curr, res, target):
        __ target __ 0:
            res.a..(l..(curr))
            r..
        ___ i __ r..(ind, l..(nums)):
            __ target < nums[i]:
                r..
            __ i > ind a.. nums[i] __ nums[i-1]:
                continue
            curr.a..(nums[i])
            helper2(nums, i+1, curr, res, target-nums[i])
            curr.pop()
    
    ___ combinationSum2_origin(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        __ n.. candidates: r.. []
        candidates.s..()
        res    # list
        helper(candidates, target, 0, [], res)
        r.. res
    
    ___ helper(self, nums, target, ind, curr, res):
        __ target __ 0:
            res.a..(l..(curr))
            r..
        prev = -1
        ___ i __ r..(ind, l..(nums)):
            __ nums[i] > target:
                r..
            __ prev != nums[i]:
                curr.a..(nums[i])
                helper(nums, target-nums[i], i+1, curr, res)
                prev = curr.pop()
