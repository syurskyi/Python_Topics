'''
Created on Apr 1, 2017

@author: MT
'''

c_ Solution(o..
    ___ getMoneyAmount  n
        dp = [[0]*(n+1) ___ _ __ r..(n+1)]
        ___ j __ r..(2, n+1
            ___ i __ r..(j-1, 0, -1
                globalMin = f__('inf')
                ___ k __ r..(i+1, j
                    localMax = k+m..(dp[i][k-1], dp[k+1][j])
                    globalMin = m..(globalMin, localMax)
                __ i+1 __ j:
                    dp[i][j] = i
                ____
                    dp[i][j] = globalMin
        r.. dp[1][n]
    
    ___ test
        testCases = [
            10,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = getMoneyAmount(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
