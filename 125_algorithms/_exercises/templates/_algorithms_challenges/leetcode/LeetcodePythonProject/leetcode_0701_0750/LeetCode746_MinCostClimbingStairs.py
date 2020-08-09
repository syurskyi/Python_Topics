'''
Created on Mar 22, 2018

@author: tongq
'''
class Solution(object
    ___ minCostClimbingStairs(self, cost
        """
        :type cost: List[int]
        :rtype: int
        """
        __ not cost: r_ 0
        __ le.(cost) __ 1: r_ cost[0]
        ___ i in range(le.(cost)):
            __ i > 1:
                cost[i] += min(cost[i-1], cost[i-2])
        r_ min(cost[-1], cost[-2])
    
    ___ test(self
        testCases = [
            [10, 15, 20],
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        ]
        ___ cost in testCases:
            result = self.minCostClimbingStairs(cost)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
