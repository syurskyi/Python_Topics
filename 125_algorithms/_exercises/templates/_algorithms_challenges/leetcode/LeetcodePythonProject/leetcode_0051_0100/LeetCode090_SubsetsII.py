'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object
    ___ subsetsWithDup(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.helper(nums, 0, [], res)
        r_ res
    
    ___ helper(self, nums, ind, curr, res
        res.append(list(curr))
        ___ i in range(ind, le.(nums)):
            __ i > ind and nums[i] __ nums[i-1]:
                continue
            curr.append(nums[i])
            self.helper(nums, i+1, curr, res)
            curr.pop()
