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
        arr = s.split(' ')
        __ len(arr) != len(pattern):
            return False
        for p, s0 in zip(pattern, arr):
            __ p in hashmap and hashmap[p] == s0:
                continue
            elif p not in hashmap and s0 not in hashset:
                hashset.add(s0)
                hashmap[p] = s0
            else:
                return False
        return True
