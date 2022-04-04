'''
Created on Apr 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ longestPalindrome  s
        hashmap    # dict
        ___ c __ s:
            hashmap[c] = hashmap.g.. c, 0)+1
        singleNum = F..
        result = 0
        ___ count __ hashmap.v..
            __ count%2 != 0:
                __ singleNum:
                    result += count-1
                ____
                    result += count
                    singleNum = T..
            ____
                result += count
        r.. result
