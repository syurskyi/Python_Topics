'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    ___ getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        __ not s1 or not s2: return 0
        res = self.countHelper(s1*(n1//n2), s2)
        res += self.countHelper(s1*(n1%n2), s2*n2)
        return res
    
    ___ countHelper(self, s1, s2):
        __ not s1 or not s2: return 0
        count = 0
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            __ s1[i] == s2[j]:
                j += 1
            i += 1
            __ j == len(s2):
                count += 1
                j = 0
        return count
