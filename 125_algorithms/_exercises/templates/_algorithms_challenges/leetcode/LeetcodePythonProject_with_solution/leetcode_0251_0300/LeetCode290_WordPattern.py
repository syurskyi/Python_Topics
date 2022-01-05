'''
Created on Mar 7, 2017

@author: MT
'''
c_ Solution(object):
    ___ wordPattern  pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashmap    # dict
        hashset = set()
        arr = s.s..(' ')
        __ l..(arr) != l..(pattern):
            r.. F..
        ___ p, s0 __ z..(pattern, arr):
            __ p __ hashmap a.. hashmap[p] __ s0:
                _____
            ____ p n.. __ hashmap a.. s0 n.. __ hashset:
                hashset.add(s0)
                hashmap[p] = s0
            ____:
                r.. F..
        r.. T..
