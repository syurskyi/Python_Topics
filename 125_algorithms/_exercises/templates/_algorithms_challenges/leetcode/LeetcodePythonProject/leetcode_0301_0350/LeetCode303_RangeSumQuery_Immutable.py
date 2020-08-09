'''
Created on Mar 11, 2017

@author: MT
'''

class NumArray(object
    ___ __init__(self, nums
        self.dp = [0]
        for num in nums:
            self.dp.append(self.dp[-1] + num)
    
    ___ sumRange(self, i, j
        r_ self.dp[j+1] - self.dp[i]
