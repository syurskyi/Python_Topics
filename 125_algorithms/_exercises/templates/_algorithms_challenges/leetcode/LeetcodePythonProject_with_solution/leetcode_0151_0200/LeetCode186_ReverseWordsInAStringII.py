'''
Created on May 17, 2018

@author: tongq
'''
class Solution(object):
    ___ reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        left = 0
        i = 0
        while i < l..(s):
            __ s[i] __ ' ':
                self.reverse(s, left, i-1)
                left = i+1
            i += 1
        self.reverse(s, left, l..(s)-1)
        self.reverse(s, 0, l..(s)-1)
    
    ___ reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
