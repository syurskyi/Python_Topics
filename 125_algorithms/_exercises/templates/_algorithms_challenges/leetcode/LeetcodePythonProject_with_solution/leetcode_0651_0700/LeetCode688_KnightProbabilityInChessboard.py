'''
Created on Oct 23, 2017

@author: MT
'''
c_ Solution(o..
    ___ knightProbability  N, K, r, c
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[1]*N ___ _ __ r..(N)]
        ___ _ __ r..(K
            dp1 = [[0]*N ___ _ __ r..(N)]
            ___ i __ r..(N
                ___ j __ r..(N
                    ___ row, col __ (i+2, j-1), (i+2, j+1),\
                        (i-2, j-1), (i-2, j+1), (i+1, j-2), (i+1, j+2),\
                        (i-1, j+2), (i-1, j-2
                        __ 0 <_ row < N a.. 0 <_ col < N:
                            dp1[i][j] += dp[row][col]
            dp = dp1
        r.. f__(dp[r][c])/8**K
    
    ___ test
        testCases = [
            [3, 2, 0, 0],
        ]
        ___ N, K, r, c __ testCases:
            print('n: %s' % N)
            print('K: %s' % K)
            print('r: %s' % r)
            print('c: %s' % c)
            result = knightProbability(N, K, r, c)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
