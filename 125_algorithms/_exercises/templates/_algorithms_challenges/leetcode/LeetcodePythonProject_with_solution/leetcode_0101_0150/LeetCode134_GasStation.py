'''
Created on Feb 8, 2017

@author: MT
'''

class Solution(object):
    ___ canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sumRemaining, sumVal, start = 0, 0, 0
        ___ i, (g, c) __ e..(z..(gas, cost)):
            remain = g-c
            __ sumRemaining >= 0:
                sumRemaining += remain
            ____:
                sumRemaining = remain
                start = i
            sumVal += remain
        __ sumVal >= 0:
            r.. start
        ____:
            r.. -1
    