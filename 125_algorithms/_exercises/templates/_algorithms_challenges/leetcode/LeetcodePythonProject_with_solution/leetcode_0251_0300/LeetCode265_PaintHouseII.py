'''
Created on Mar 3, 2017

@author: MT
'''

c_ Solution(o..):
    ___ minCostII  costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        __ n.. costs: r.. 0
        n, k = l..(costs), l..(costs[0])
        minInd1, minInd2 = -1, -1
        ___ i __ r..(n):
            last1, last2 = minInd1, minInd2
            minInd1, minInd2 = -1, -1
            ___ j __ r..(k):
                __ j != last1:
                    costs[i][j] += 0 __ last1 < 0 ____ costs[i-1][last1]
                ____:
                    costs[i][j] += 0 __ last2 < 0 ____ costs[i-1][last2]
                __ minInd1 < 0 o. costs[i][j] < costs[i][minInd1]:
                    minInd2 = minInd1
                    minInd1 = j
                ____ minInd2 < 0 o. costs[i][j] < costs[i][minInd2]:
                    minInd2 = j
        r.. costs[-1][minInd1]
    
    ___ minCostII_slow  costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        __ n.. costs: r.. 0
        n = l..(costs)
        k = l..(costs[0])
        ___ i __ r..(1, n):
            ___ j __ r..(k):
                minList    # list
                ___ l __ r..(k):
                    __ j != l:
                        minList.a..(costs[i-1][l])
                costs[i][j] += m..(minList)
        r.. m..(costs[-1])
    
    ___ test
        testCases = [
            [[1,5,3],[2,9,4]],
        ]
        ___ costs __ testCases:
            print('costs: %s' % costs)
            result = minCostII(costs)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
