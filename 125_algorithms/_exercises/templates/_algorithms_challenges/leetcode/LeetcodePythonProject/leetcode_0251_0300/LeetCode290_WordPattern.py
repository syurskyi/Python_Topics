'''
Created on Mar 7, 2017

@author: MT
'''
class Solution(object
    ___ wordPattern(self, pattern, s
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashmap = {}
        hashset = set()
        arr = s.split(' ')
        __ le.(arr) != le.(pattern
            r_ False
        for p, s0 in zip(pattern, arr
            __ p in hashmap and hashmap[p] __ s0:
                continue
            ____ p not in hashmap and s0 not in hashset:
                hashset.add(s0)
                hashmap[p] = s0
            ____
                r_ False
        r_ True
