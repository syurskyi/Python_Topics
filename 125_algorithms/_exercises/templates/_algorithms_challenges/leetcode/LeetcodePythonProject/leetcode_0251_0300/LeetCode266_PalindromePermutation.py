'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object
    ___ canPermutePalindrome(self, s
        __ not s: r_ False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        for value in hashmap.values(
            __ value%2 != 0:
                odd += 1
        __ le.(s)%2 __ 0:
            r_ bool(odd __ 0)
        ____
            r_ bool(odd < 2)