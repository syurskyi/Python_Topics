'''
Created on Apr 5, 2017

@author: MT
'''

class Solution(object):
    ___ __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    ___ pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        _______ random
        count = 0
        res = -1
        ___ i, num __ e..(self.nums):
            __ target __ num:
                __ random.randint(0, count) __ 0:
                    res = i
                count += 1
        r.. res
