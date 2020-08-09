'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object
    ___ hIndex(self, citations
        """
        :type citations: List[int]
        :rtype: int
        """
        n = le.(citations)
        count = [0]*(n+1)
        ___ c in citations:
            __ c >= n:
                count[n] += 1
            ____
                count[c] += 1
        res = 0
        sumVal = 0
        ___ i in range(n, -1, -1
            sumVal += count[i]
            __ sumVal >= i:
                r_ i
        r_ res
