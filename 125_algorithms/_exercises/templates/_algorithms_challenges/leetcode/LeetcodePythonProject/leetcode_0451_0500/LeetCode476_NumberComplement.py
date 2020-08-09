'''
Created on Apr 27, 2017

@author: MT
'''
class Solution(
    ___ findComplement(self, num
        i = 1
        w___ i <= num:
            i = i << 1
        r_ (i-1) ^ num
    
    ___ findComplement_another(self, num
        result = 0
        start = False
        for i in range(31, -1, -1
            first = (num >> i)&1
            __ first __ 1 and start __ False:
                start = True
            __ start:
                __ first __ 0:
                    result += (1 << i)
        r_ result
