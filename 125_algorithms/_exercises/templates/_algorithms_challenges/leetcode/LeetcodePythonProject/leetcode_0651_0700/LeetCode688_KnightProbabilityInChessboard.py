'''
Created on Oct 23, 2017

@author: MT
'''
class Solution(object
    ___ knightProbability(self, N, K, r, c
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[1]*N ___ _ in range(N)]
        ___ _ in range(K
            dp1 = [[0]*N ___ _ in range(N)]
            ___ i in range(N
                ___ j in range(N
                    ___ row, col in (i+2, j-1), (i+2, j+1),\
                        (i-2, j-1), (i-2, j+1), (i+1, j-2), (i+1, j+2),\
                        (i-1, j+2), (i-1, j-2
                        __ 0 <= row < N and 0 <= col < N:
                            dp1[i][j] += dp[row][col]
            dp = dp1
        r_ float(dp[r][c])/8**K
    
    ___ test(self
        testCases = [
            [3, 2, 0, 0],
        ]
        ___ N, K, r, c in testCases:
            print('n: %s' % N)
            print('K: %s' % K)
            print('r: %s' % r)
            print('c: %s' % c)
            result = self.knightProbability(N, K, r, c)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
