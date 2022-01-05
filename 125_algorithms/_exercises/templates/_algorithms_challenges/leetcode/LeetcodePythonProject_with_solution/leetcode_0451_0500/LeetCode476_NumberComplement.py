'''
Created on Apr 27, 2017

@author: MT
'''
c_ Solution
    ___ findComplement  num):
        i = 1
        w.... i <= num:
            i = i << 1
        r.. (i-1) ^ num
    
    ___ findComplement_another  num):
        result = 0
        start = F..
        ___ i __ r..(31, -1, -1):
            first = (num >> i)&1
            __ first __ 1 a.. start __ F..:
                start = T..
            __ start:
                __ first __ 0:
                    result += (1 << i)
        r.. result
