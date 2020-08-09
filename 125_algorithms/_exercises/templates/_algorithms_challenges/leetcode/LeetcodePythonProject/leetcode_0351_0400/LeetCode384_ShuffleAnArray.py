'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object
    ___ __init__(self, nums
        self.nums = nums
    
    ___ reset(self
        r_ self.nums
    
    ___ shuffle(self
        ______ random
        newNums = list(self.nums)
        __ not newNums:
            r_ newNums
        ___ i in range(le.(newNums)-1, 0, -1
            ind = random.randint(0, i)
            newNums[ind], newNums[i] = newNums[i], newNums[ind]
        r_ newNums
