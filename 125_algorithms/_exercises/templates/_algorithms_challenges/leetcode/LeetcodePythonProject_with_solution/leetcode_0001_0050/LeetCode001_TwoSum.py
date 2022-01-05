'''
Created on Nov 8, 2017

@author: MT
'''
c_ Solution(object):
    ___ twoSum  nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap    # dict
        res    # list
        ___ i, num __ e..(nums):
            __ target-num __ hashmap:
                r.. [hashmap[target-num], i]
            hashmap[num] = i
        r.. res
