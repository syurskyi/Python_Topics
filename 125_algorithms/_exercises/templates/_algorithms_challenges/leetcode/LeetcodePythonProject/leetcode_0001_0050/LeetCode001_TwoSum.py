'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object
    ___ twoSum(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        res = []
        ___ i, num in enumerate(nums
            __ target-num in hashmap:
                r_ [hashmap[target-num], i]
            hashmap[num] = i
        r_ res
