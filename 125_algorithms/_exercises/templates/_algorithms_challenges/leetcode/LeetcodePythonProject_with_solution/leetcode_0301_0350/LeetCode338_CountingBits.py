'''
Created on Mar 20, 2017

@author: MT
'''
class Solution(object):
    ___ countBits(self, num):
        result = [0]*(num+1)
        ___ i __ r..(1, num+1):
            result[i] = result[i>>1]+(i&1)
        r.. result
