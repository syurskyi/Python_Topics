'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object
    ___ strStr(self, haystack, needle
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        __ haystack __ needle or not needle: r_ 0
        ___ i in range(le.(haystack)-le.(needle)+1
            ___ j in range(le.(needle)):
                __ haystack[i+j] __ needle[j]:
                    __ j __ le.(needle)-1:
                        r_ i
                ____
                    break
        r_ -1
