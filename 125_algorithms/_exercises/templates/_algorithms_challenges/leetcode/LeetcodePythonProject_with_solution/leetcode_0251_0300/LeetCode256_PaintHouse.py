'''
Created on Mar 1, 2017

@author: MT
'''

c_ Solution(object):
    ___ minCost  costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        __ n.. costs: r.. 0
        ___ i __ r..(1, l..(costs)):
            costs[i][0] += m..(costs[i-1][1], costs[i-1][2])
            costs[i][1] += m..(costs[i-1][0], costs[i-1][2])
            costs[i][2] += m..(costs[i-1][0], costs[i-1][1])
        r.. m..(costs[-1])
