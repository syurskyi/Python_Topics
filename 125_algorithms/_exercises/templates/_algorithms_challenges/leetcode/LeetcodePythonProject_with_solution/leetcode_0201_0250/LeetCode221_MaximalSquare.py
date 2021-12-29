'''
Created on Feb 21, 2017

@author: MT
'''

class Solution(object):
    ___ maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        __ not matrix: return 0
        maxLen = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                __ matrix[i][j] == '1':
                    dp[i+1][j+1] = min([dp[i][j], dp[i+1][j], dp[i][j+1]])+1
                    maxLen = max(maxLen, dp[i+1][j+1])
        return maxLen*maxLen
    
    ___ test(self):
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
        for matrix in testCases:
            print('matrix: %s' % matrix)
            matrix = [list(x) for x in matrix]
            result = self.maximalSquare(matrix)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ == '__main__':
    Solution().test()
