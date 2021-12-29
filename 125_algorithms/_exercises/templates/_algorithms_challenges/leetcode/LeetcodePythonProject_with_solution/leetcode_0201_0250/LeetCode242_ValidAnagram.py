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
        __ not s and not t: return True
        __ not s or not t: return False
        __ len(s) != len(t): return False
        hashmap = {}
        for c in s:
            __ c in hashmap: hashmap[c] += 1
            else: hashmap[c] = 1
        for c in t:
            __ c not in hashmap: return False
            hashmap[c] -= 1
            __ hashmap[c] == 0:
                del hashmap[c]
        __ hashmap:
            return False
        return True
    
    