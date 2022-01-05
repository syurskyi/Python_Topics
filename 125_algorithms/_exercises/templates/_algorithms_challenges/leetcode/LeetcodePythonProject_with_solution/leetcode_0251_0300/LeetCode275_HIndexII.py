'''
Created on Mar 5, 2017

@author: MT
'''

c_ Solution(object):
    ___ hIndex  citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = l..(citations)
        count = [0]*(n+1)
        ___ c __ citations:
            __ c >= n:
                count[n] += 1
            ____:
                count[c] += 1
        res = 0
        sumVal = 0
        ___ i __ r..(n, -1, -1):
            sumVal += count[i]
            __ sumVal >= i:
                r.. i
        r.. res
