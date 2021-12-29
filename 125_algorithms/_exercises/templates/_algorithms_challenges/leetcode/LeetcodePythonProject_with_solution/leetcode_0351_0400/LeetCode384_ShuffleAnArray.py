'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    ___ __init__(self, nums):
        self.nums = nums
    
    ___ reset(self):
        return self.nums
    
    ___ shuffle(self):
        import random
        newNums = list(self.nums)
        __ not newNums:
            return newNums
        for i in range(len(newNums)-1, 0, -1):
            ind = random.randint(0, i)
            newNums[ind], newNums[i] = newNums[i], newNums[ind]
        return newNums
