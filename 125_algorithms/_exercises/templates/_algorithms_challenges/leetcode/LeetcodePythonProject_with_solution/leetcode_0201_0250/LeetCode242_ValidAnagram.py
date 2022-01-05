'''
Created on Feb 27, 2017

@author: MT
'''

c_ Solution(o..):
    ___ isAnagram  s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ n.. s a.. n.. t: r.. T..
        __ n.. s o. n.. t: r.. F..
        __ l..(s) != l..(t): r.. F..
        hashmap    # dict
        ___ c __ s:
            __ c __ hashmap: hashmap[c] += 1
            ____: hashmap[c] = 1
        ___ c __ t:
            __ c n.. __ hashmap: r.. F..
            hashmap[c] -= 1
            __ hashmap[c] __ 0:
                del hashmap[c]
        __ hashmap:
            r.. F..
        r.. T..
    
    