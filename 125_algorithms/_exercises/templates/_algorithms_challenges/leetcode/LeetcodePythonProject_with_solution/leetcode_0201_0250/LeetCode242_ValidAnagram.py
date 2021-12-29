'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object):
    ___ isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ n.. s a.. n.. t: r.. True
        __ n.. s o. n.. t: r.. False
        __ l..(s) != l..(t): r.. False
        hashmap = {}
        ___ c __ s:
            __ c __ hashmap: hashmap[c] += 1
            ____: hashmap[c] = 1
        ___ c __ t:
            __ c n.. __ hashmap: r.. False
            hashmap[c] -= 1
            __ hashmap[c] __ 0:
                del hashmap[c]
        __ hashmap:
            r.. False
        r.. True
    
    