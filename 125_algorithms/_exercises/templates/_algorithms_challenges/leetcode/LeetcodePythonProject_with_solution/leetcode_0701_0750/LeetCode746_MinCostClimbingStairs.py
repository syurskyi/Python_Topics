'''
Created on Mar 22, 2018

@author: tongq
'''
class Solution(object):
    ___ minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        __ not cost: return 0
        __ len(cost) == 1: return cost[0]
        for i in range(len(cost)):
            __ i > 1:
                cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
    
    ___ test(self):
        testCases = [
            [10, 15, 20],
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        ]
        for cost in testCases:
            result = self.minCostClimbingStairs(cost)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
