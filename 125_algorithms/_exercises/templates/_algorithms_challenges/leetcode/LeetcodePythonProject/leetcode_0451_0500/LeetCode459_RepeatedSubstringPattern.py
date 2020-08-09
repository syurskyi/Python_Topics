'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object
    ___ repeatedSubstringPattern(self, s
        n = le.(s)
        for i in range(1, n//2+2
            sub = s[:i]
            __ le.(s)%le.(sub) __ 0:
                j = i
                w___ j+le.(sub) <= n and s[j:j+le.(sub)]__sub:
                    j += le.(sub)
                    __ j __ n:
                        r_ True
        r_ False
