'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object
    ___ longestPalindrome(self, s
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        singleNum = False
        result = 0
        for count in hashmap.values(
            __ count%2 != 0:
                __ singleNum:
                    result += count-1
                ____
                    result += count
                    singleNum = True
            ____
                result += count
        r_ result
