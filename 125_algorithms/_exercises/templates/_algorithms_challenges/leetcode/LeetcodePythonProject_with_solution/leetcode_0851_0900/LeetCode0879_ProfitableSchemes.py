'''
Created on Oct 14, 2019

@author: tongq
'''
class Solution(object):
    ___ profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0]*(G+1) ___ _ __ r..(P+1)]
        dp[0][0] = 1
        ___ p, g __ zip(profit, group):
            ___ i __ r..(P, -1, -1):
                ___ j __ r..(G-g, -1, -1):
                    dp[m..(i+p, P)][j+g] += dp[i][j]
        r.. s..(dp[P])%(10**9 + 7)
    
    ___ profitableSchemes_DFS_TLE(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        res = [0]
        self.dfs(0, group, profit, G, P, [], 0, res)
        r.. res[0]
    
    ___ dfs(self, ind, group, profit, G, P, curGroup, curProfit, res):
        __ curProfit >= P and s..(curGroup) <= G:
            res[0] += 1
        ___ i __ r..(ind, l..(group)):
            curProfit += profit[i]
            curGroup.a..(group[i])
            self.dfs(i+1, group, profit, G, P, curGroup, curProfit, res)
            curGroup.pop()
            curProfit -= profit[i]
    
    ___ test(self):
        testCases = [
            [
                5, 3, [2,2], [2,3]
            ],
            [
                10, 5, [2,3,5], [6,7,8]
            ],
        ]
        ___ G, P, group, profit __ testCases:
            res = self.profitableSchemes(G, P, group, profit)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
