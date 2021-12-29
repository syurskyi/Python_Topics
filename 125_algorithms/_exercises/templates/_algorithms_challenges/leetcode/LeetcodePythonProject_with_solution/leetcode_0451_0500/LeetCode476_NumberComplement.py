'''
Created on Apr 27, 2017

@author: MT
'''
class Solution():
    ___ findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        r.. (i-1) ^ num
    
    ___ findComplement_another(self, num):
        result = 0
        start = False
        ___ i __ r..(31, -1, -1):
            first = (num >> i)&1
            __ first __ 1 and start __ False:
                start = True
            __ start:
                __ first __ 0:
                    result += (1 << i)
        r.. result
