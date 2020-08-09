'''
Created on Mar 3, 2017

@author: MT
'''

class Solution(object
    ___ minCostII(self, costs
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        __ not costs: r_ 0
        n, k = le.(costs), le.(costs[0])
        minInd1, minInd2 = -1, -1
        for i in range(n
            last1, last2 = minInd1, minInd2
            minInd1, minInd2 = -1, -1
            for j in range(k
                __ j != last1:
                    costs[i][j] += 0 __ last1 < 0 else costs[i-1][last1]
                ____
                    costs[i][j] += 0 __ last2 < 0 else costs[i-1][last2]
                __ minInd1 < 0 or costs[i][j] < costs[i][minInd1]:
                    minInd2 = minInd1
                    minInd1 = j
                ____ minInd2 < 0 or costs[i][j] < costs[i][minInd2]:
                    minInd2 = j
        r_ costs[-1][minInd1]
    
    ___ minCostII_slow(self, costs
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        __ not costs: r_ 0
        n = le.(costs)
        k = le.(costs[0])
        for i in range(1, n
            for j in range(k
                minList = []
                for l in range(k
                    __ j != l:
                        minList.append(costs[i-1][l])
                costs[i][j] += min(minList)
        r_ min(costs[-1])
    
    ___ test(self
        testCases = [
            [[1,5,3],[2,9,4]],
        ]
        for costs in testCases:
            print('costs: %s' % costs)
            result = self.minCostII(costs)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
