'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object
    ___ isAnagram(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ not s and not t: r_ True
        __ not s or not t: r_ False
        __ le.(s) != le.(t r_ False
        hashmap = {}
        for c in s:
            __ c in hashmap: hashmap[c] += 1
            ____ hashmap[c] = 1
        for c in t:
            __ c not in hashmap: r_ False
            hashmap[c] -= 1
            __ hashmap[c] __ 0:
                del hashmap[c]
        __ hashmap:
            r_ False
        r_ True
    
    