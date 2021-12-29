'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object):
    ___ twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        res    # list
        ___ i, num __ enumerate(nums):
            __ target-num __ hashmap:
                r.. [hashmap[target-num], i]
            hashmap[num] = i
        r.. res
