'''
Created on Aug 23, 2017

@author: MT
'''

class Solution(object
    ___ checkRecord(self, n
        """
        :type n: int
        :rtype: int
        """
        ______ numpy
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
        w___ n:
            __ n & 1:
                power = (power*matrix)%mod
            matrix = matrix**2 % mod
            n /= 2
        r_ int(power[5, 2])
    
    ___ checkRecord_slow(self, n
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [[[0]*3 ___ _ __ range(2)] ___ _ __ range(n+1)]
        ___ i __ range(2
            ___ j __ range(3
                dp[0][i][j] = 1
        ___ i __ range(1, n+1
            ___ j __ range(2
                ___ k __ range(3
                    val = dp[i-1][j][2]
                    __ j > 0:
                        val = (val+dp[i-1][j-1][2]) % mod # A
                    __ k > 0:
                        val = (val+dp[i-1][j][k-1]) % mod # L
                    dp[i][j][k] = val
        r_ dp[-1][-1][-1]
    
    ___ test(self
        testCases = [
            2,
            3,
            4,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = self.checkRecord(n)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
