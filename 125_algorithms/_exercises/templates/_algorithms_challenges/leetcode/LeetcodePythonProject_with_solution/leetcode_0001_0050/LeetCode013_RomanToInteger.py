'''
Created on Nov 7, 2017

@author: MT
'''
c_ Solution(object):
    ___ romanToInt  s):
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        ___ i, c __ e..(s):
            curVal = hashmap[c]
            __ i+1 < l..(s) a.. hashmap[s[i+1]] > curVal:
                res -= curVal
            ____:
                res += curVal
        r.. res
