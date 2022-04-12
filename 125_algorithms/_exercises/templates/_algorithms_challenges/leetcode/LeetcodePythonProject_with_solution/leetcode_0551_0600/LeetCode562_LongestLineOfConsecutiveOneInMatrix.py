'''
Created on Aug 29, 2017

@author: MT
'''
c_ Solution(o..
    ___ longestLine  M
        """
        :type M: List[List[int]]
        :rtype: int
        """
        matrix M
        __ n.. matrix o. n.. matrix[0]: r.. 0
        maxLen 0
        m, n l..(matrix), l..(matrix 0
        dp [[[0]*4 ___ _ __ r..(n)] ___ _ __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ matrix[i][j] __ 0:
                    _____
                ___ k __ r..(4
                    dp[i][j][k] 1
                __ j > 0:
                    dp[i][j][0] += dp[i][j-1][0]
                __ j > 0 a.. i > 0:
                    dp[i][j][1] += dp[i-1][j-1][1]
                __ i > 0:
                    dp[i][j][2] += dp[i-1][j][2]
                __ i > 0 a.. j+1 < n:
                    dp[i][j][3] += dp[i-1][j+1][3]
                maxLen m..(maxLen, dp[i][j][0], dp[i][j][1],\
                             dp[i][j][2], dp[i][j][3])
        r.. maxLen
    
    ___ test
        testCases [
            [
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,1],
            ],
        ]
        ___ matrix __ testCases:
            print('\n'.j..([s..(row) ___ row __ matrix]
            result longestLine(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
