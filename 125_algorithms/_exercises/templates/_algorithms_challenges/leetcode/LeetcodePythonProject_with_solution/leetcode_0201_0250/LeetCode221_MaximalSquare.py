'''
Created on Feb 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ maximalSquare  matrix
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        __ n.. matrix: r.. 0
        maxLen = 0
        m, n = l..(matrix), l..(matrix[0])
        dp = [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ matrix[i][j] __ '1':
                    dp[i+1][j+1] = m..([dp[i][j], dp[i+1][j], dp[i][j+1]])+1
                    maxLen = m..(maxLen, dp[i+1][j+1])
        r.. maxLen*maxLen
    
    ___ test
        testCases = [
            [
                '111',
            ],
            [
                '10100',
                '10111',
                '11111',
                '10010',
            ],
        ]
        ___ matrix __ testCases:
            print('matrix: %s' % matrix)
            matrix = [l..(x) ___ x __ matrix]
            result = maximalSquare(matrix)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
