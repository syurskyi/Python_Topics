'''
Created on Feb 16, 2017

@author: MT
'''

class Solution:
    # @param n, an integer
    # @return an integer
    ___ reverseBits(self, n):
        res = 0
        ___ i __ r..(0, 32):
            last = n >> i
            res = res << 1
            res |= last & 1
        r.. res
