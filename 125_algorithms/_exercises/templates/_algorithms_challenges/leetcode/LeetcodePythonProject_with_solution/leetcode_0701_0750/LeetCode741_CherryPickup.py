'''
Created on Mar 20, 2018

@author: tongq
'''
c_ Solution(object):
    ___ cherryPickup  grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = l..(grid)
        M = (N<<1)-1
        dp = [[0]*N ___ _ __ r..(N)]
        dp[0][0] = grid[0][0]
        ___ n __ r..(1, M):
            ___ i __ r..(N-1, -1, -1):
                ___ p __ r..(N-1, -1, -1):
                    j = n-i
                    q = n-p
                    __ j<0 o. j>=N o. q<0 o. q>=N o. grid[i][j]<0 o. grid[p][q]<0:
                        dp[i][p] = -1
                        _____
                    __ i > 0:
                        dp[i][p] = m..(dp[i][p], dp[i-1][p])
                    __ p > 0:
                        dp[i][p] = m..(dp[i][p], dp[i][p-1])
                    __ i > 0 a.. p > 0:
                        dp[i][p] = m..(dp[i][p], dp[i-1][p-1])
                    __ dp[i][p] >= 0:
                        dp[i][p] += grid[i][j]+(grid[p][q] __ i!=p ____ 0)
        r.. m..(dp[-1][-1], 0)
    
    ___ test
        testCases = [
            [
                [0, 1, -1],
                [1, 0, -1],
                [1, 1,  1]
            ],
        ]
        ___ grid __ testCases:
            result = cherryPickup(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
