'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    ___ canPermutePalindrome(self, s):
        __ not s: return False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        for value in hashmap.values():
            __ value%2 != 0:
                odd += 1
        __ len(s)%2 == 0:
            return bool(odd == 0)
        else:
            return bool(odd < 2)