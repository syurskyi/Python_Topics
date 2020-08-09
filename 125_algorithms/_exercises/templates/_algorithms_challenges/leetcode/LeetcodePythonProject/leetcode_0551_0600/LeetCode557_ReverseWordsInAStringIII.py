'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object
    ___ reverseWords(self, s
        """
        :type s: str
        :rtype: str
        """
        res = ''
        prev = 0
        ___ i, c in enumerate(s
            __ c __ ' ':
                tmpRes = self.reverse(s, prev, i-1)
                res += tmpRes + ' '
                prev = i+1
        tmpRes = self.reverse(s, prev, le.(s)-1)
        res += tmpRes
        r_ res
    
    ___ reverse(self, s, i, j
        res = ''
        w___ i <= j:
            res += s[j]
            j -= 1
        r_ res
