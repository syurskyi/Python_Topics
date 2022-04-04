'''
Created on Mar 22, 2018

@author: tongq
'''
c_ Solution(o..
    ___ minCostClimbingStairs  cost
        """
        :type cost: List[int]
        :rtype: int
        """
        __ n.. cost: r.. 0
        __ l..(cost) __ 1: r.. cost[0]
        ___ i __ r..(l..(cost:
            __ i > 1:
                cost[i] += m..(cost[i-1], cost[i-2])
        r.. m..(cost[-1], cost[-2])
    
    ___ test
        testCases = [
            [10, 15, 20],
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        ]
        ___ cost __ testCases:
            result = minCostClimbingStairs(cost)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
