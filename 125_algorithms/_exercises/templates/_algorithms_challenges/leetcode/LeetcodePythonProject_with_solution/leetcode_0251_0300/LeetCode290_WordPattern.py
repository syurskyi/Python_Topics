'''
Created on Mar 7, 2017

@author: MT
'''
class Solution(object):
    ___ wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashmap = {}
        hashset = set()
        arr = s.s..(' ')
        __ l..(arr) != l..(pattern):
            r.. False
        ___ p, s0 __ z..(pattern, arr):
            __ p __ hashmap a.. hashmap[p] __ s0:
                continue
            ____ p n.. __ hashmap a.. s0 n.. __ hashset:
                hashset.add(s0)
                hashmap[p] = s0
            ____:
                r.. False
        r.. True
