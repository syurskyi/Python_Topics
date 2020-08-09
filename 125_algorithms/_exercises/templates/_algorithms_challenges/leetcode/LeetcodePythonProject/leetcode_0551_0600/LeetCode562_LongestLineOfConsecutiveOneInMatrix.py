'''
Created on Aug 29, 2017

@author: MT
'''
class Solution(object
    ___ longestLine(self, M
        """
        :type M: List[List[int]]
        :rtype: int
        """
        matrix = M
        __ not matrix or not matrix[0]: r_ 0
        maxLen = 0
        m, n = le.(matrix), le.(matrix[0])
        dp = [[[0]*4 for _ in range(n)] for _ in range(m)]
        for i in range(m
            for j in range(n
                __ matrix[i][j] __ 0:
                    continue
                for k in range(4
                    dp[i][j][k] = 1
                __ j > 0:
                    dp[i][j][0] += dp[i][j-1][0]
                __ j > 0 and i > 0:
                    dp[i][j][1] += dp[i-1][j-1][1]
                __ i > 0:
                    dp[i][j][2] += dp[i-1][j][2]
                __ i > 0 and j+1 < n:
                    dp[i][j][3] += dp[i-1][j+1][3]
                maxLen = max(maxLen, dp[i][j][0], dp[i][j][1],\
                             dp[i][j][2], dp[i][j][3])
        r_ maxLen
    
    ___ test(self
        testCases = [
            [
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,1],
            ],
        ]
        for matrix in testCases:
            print('\n'.join([str(row) for row in matrix]))
            result = self.longestLine(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
