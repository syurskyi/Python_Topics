'''
Created on Oct 14, 2019

@author: tongq
'''
c_ Solution(o..
    ___ profitableSchemes  G, P, group, profit
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp [[0]*(G+1) ___ _ __ r..(P+1)]
        dp 0 0  1
        ___ p, g __ z..(profit, group
            ___ i __ r..(P, -1, -1
                ___ j __ r..(G-g, -1, -1
                    dp[m..(i+p, P)][j+g] += dp[i][j]
        r.. s..(dp[P])%(10**9 + 7)
    
    ___ profitableSchemes_DFS_TLE  G, P, group, profit
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        res [0]
        dfs(0, group, profit, G, P, [], 0, res)
        r.. res[0]
    
    ___ dfs  ind, group, profit, G, P, curGroup, curProfit, res
        __ curProfit >_ P a.. s..(curGroup) <_ G:
            res[0] += 1
        ___ i __ r..(ind, l..(group:
            curProfit += profit[i]
            curGroup.a..(group[i])
            dfs(i+1, group, profit, G, P, curGroup, curProfit, res)
            curGroup.p.. )
            curProfit -_ profit[i]
    
    ___ test
        testCases [
            [
                5, 3, [2,2], [2,3]
            ],
            [
                10, 5, [2,3,5], [6,7,8]
            ],
        ]
        ___ G, P, group, profit __ testCases:
            res profitableSchemes(G, P, group, profit)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
