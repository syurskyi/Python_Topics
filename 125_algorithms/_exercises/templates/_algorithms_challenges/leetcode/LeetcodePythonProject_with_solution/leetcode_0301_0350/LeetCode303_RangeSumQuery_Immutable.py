'''
Created on Mar 11, 2017

@author: MT
'''

class NumArray(object):
    ___ __init__(self, nums):
        self.dp = [0]
        ___ num __ nums:
            self.dp.a..(self.dp[-1] + num)
    
    ___ sumRange(self, i, j):
        r.. self.dp[j+1] - self.dp[i]
