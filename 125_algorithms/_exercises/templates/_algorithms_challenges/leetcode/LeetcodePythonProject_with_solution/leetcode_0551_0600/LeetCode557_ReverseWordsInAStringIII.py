'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object):
    ___ reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        prev = 0
        for i, c in enumerate(s):
            __ c == ' ':
                tmpRes = self.reverse(s, prev, i-1)
                res += tmpRes + ' '
                prev = i+1
        tmpRes = self.reverse(s, prev, len(s)-1)
        res += tmpRes
        return res
    
    ___ reverse(self, s, i, j):
        res = ''
        while i <= j:
            res += s[j]
            j -= 1
        return res
