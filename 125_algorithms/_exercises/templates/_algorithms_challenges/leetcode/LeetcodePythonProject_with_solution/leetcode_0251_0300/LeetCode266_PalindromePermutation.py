'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    ___ canPermutePalindrome(self, s):
        __ n.. s: r.. False
        hashmap = {}
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        ___ value __ hashmap.values():
            __ value%2 != 0:
                odd += 1
        __ l..(s)%2 __ 0:
            r.. bool(odd __ 0)
        ____:
            r.. bool(odd < 2)