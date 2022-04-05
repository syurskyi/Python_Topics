'''
Created on Aug 28, 2017

@author: MT
'''

c_ Solution(o..
    ___ reverseWords  s
        """
        :type s: str
        :rtype: str
        """
        res = ''
        prev = 0
        ___ i, c __ e..(s
            __ c __ ' ':
                tmpRes = reverse(s, prev, i-1)
                res += tmpRes + ' '
                prev = i+1
        tmpRes = reverse(s, prev, l..(s)-1)
        res += tmpRes
        r.. res
    
    ___ reverse  s, i, j
        res = ''
        w.... i <_ j:
            res += s[j]
            j -_ 1
        r.. res
