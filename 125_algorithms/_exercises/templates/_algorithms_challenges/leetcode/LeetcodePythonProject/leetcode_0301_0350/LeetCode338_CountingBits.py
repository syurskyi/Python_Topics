'''
Created on Mar 20, 2017

@author: MT
'''
class Solution(object
    ___ countBits(self, num
        result = [0]*(num+1)
        ___ i in range(1, num+1
            result[i] = result[i>>1]+(i&1)
        r_ result
