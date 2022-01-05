'''
Created on Apr 2, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ orderOfLargestPlusSign  N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        n = N
        matrix = [[1]*n ___ _ __ r..(n)]
        ___ i, j __ mines:
            matrix[i][j] = 0
        maxLen = 0
        dp = [[[0]*4 ___ _ __ r..(n)] ___ _ __ r..(n)]
        ___ i __ r..(n):
            ___ j __ r..(n):
                __ matrix[i][j] __ 0:
                    _____
                __ i __ 0 a.. j __ 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = 1
                ____ i __ 0 a.. j != 0:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = 1
                ____ i != 0 a.. j __ 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = dp[i-1][j][1]+1
                ____:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = dp[i-1][j][1]+1
        ___ i __ r..(n-1, -1, -1):
            ___ j __ r..(n-1, -1, -1):
                __ matrix[i][j] __ 0:
                    _____
                __ i __ n-1 a.. j __ n-1:
                    dp[i][j][2] = 1
                    dp[i][j][3] = 1
                ____ i __ n-1 a.. j != n-1:
                    dp[i][j][2] = 1
                    dp[i][j][3] = dp[i][j+1][3]+1
                ____ i != n-1 a.. j __ n-1:
                    dp[i][j][2] = dp[i+1][j][2]+1
                    dp[i][j][3] = 1
                ____:
                    dp[i][j][2] = dp[i+1][j][2]+1
                    dp[i][j][3] = dp[i][j+1][3]+1
        ___ i __ r..(n):
            ___ j __ r..(n):
                maxLen = m..(maxLen, m..(dp[i][j]))
        r.. maxLen
    
    ___ test
        testCases = [
            [5, [[4, 2]]],
            [2, []],
            [1, [[0, 0]]],
            [2, [[0, 0], [1,1]]],
            [5, [[3,0],[3,3]]],
            [5, [[0,1],[0,2],[1,0],[1,2],[1,4],[2,0],[2,2],[3,0],[3,1],[4,0],[4,1],[4,3],[4,4]]],
        ]
        ___ n, mines __ testCases:
            print('n: %s' % n)
            print('mines: %s' % mines)
            result = orderOfLargestPlusSign(n, mines)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
