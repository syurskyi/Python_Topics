'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    ___ __init__(self, nums):
        self.nums = nums
    
    ___ reset(self):
        r.. self.nums
    
    ___ shuffle(self):
        _______ random
        newNums = l..(self.nums)
        __ n.. newNums:
            r.. newNums
        ___ i __ r..(l..(newNums)-1, 0, -1):
            ind = random.randint(0, i)
            newNums[ind], newNums[i] = newNums[i], newNums[ind]
        r.. newNums
