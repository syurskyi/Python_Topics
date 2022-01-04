'''
Created on Aug 23, 2017

@author: MT
'''

c_ Solution(object):
    ___ checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        _______ numpy
        matrix = numpy.matrix(
            [
                [0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 1],
            ]
        )
        power = matrix
        mod = 10**9+7
        w.... n:
            __ n & 1:
                power = (power*matrix)%mod
            matrix = matrix**2 % mod
            n /= 2
        r.. i..(power[5, 2])
    
    ___ checkRecord_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [[[0]*3 ___ _ __ r..(2)] ___ _ __ r..(n+1)]
        ___ i __ r..(2):
            ___ j __ r..(3):
                dp[0][i][j] = 1
        ___ i __ r..(1, n+1):
            ___ j __ r..(2):
                ___ k __ r..(3):
                    val = dp[i-1][j][2]
                    __ j > 0:
                        val = (val+dp[i-1][j-1][2]) % mod # A
                    __ k > 0:
                        val = (val+dp[i-1][j][k-1]) % mod # L
                    dp[i][j][k] = val
        r.. dp[-1][-1][-1]
    
    ___ test
        testCases = [
            2,
            3,
            4,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = checkRecord(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
