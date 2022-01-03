'''
Created on Apr 25, 2017

@author: MT
'''

c_ Solution(object):
    ___ getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        __ n.. s1 o. n.. s2: r.. 0
        res = countHelper(s1*(n1//n2), s2)
        res += countHelper(s1*(n1%n2), s2*n2)
        r.. res
    
    ___ countHelper(self, s1, s2):
        __ n.. s1 o. n.. s2: r.. 0
        count = 0
        i, j = 0, 0
        w.... i < l..(s1) a.. j < l..(s2):
            __ s1[i] __ s2[j]:
                j += 1
            i += 1
            __ j __ l..(s2):
                count += 1
                j = 0
        r.. count
