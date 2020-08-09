'''
Created on Mar 1, 2017

@author: MT
'''

class Solution(object
    ___ minCost(self, costs
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        __ not costs: r_ 0
        ___ i in range(1, le.(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        r_ min(costs[-1])
