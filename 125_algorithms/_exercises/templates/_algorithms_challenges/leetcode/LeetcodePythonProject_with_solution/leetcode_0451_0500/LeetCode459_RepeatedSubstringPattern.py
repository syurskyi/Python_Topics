'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    ___ repeatedSubstringPattern(self, s):
        n = l..(s)
        ___ i __ r..(1, n//2+2):
            sub = s[:i]
            __ l..(s)%l..(sub) __ 0:
                j = i
                while j+l..(sub) <= n and s[j:j+l..(sub)]__sub:
                    j += l..(sub)
                    __ j __ n:
                        r.. True
        r.. False
