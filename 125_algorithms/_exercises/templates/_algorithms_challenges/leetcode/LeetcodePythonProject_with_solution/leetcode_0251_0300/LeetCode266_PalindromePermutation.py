'''
Created on Mar 4, 2017

@author: MT
'''

c_ Solution(o..):
    ___ canPermutePalindrome  s):
        __ n.. s: r.. F..
        hashmap    # dict
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        ___ value __ hashmap.v..
            __ value%2 != 0:
                odd += 1
        __ l..(s)%2 __ 0:
            r.. bool(odd __ 0)
        ____:
            r.. bool(odd < 2)