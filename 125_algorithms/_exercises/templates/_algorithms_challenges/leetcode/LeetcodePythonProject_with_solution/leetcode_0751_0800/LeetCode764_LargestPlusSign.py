'''
Created on Apr 2, 2018

@author: tongq
'''
class Solution(object):
    ___ orderOfLargestPlusSign(self, N, mines):
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
                    continue
                __ i __ 0 and j __ 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = 1
                ____ i __ 0 and j != 0:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = 1
                ____ i != 0 and j __ 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = dp[i-1][j][1]+1
                ____:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = dp[i-1][j][1]+1
        ___ i __ r..(n-1, -1, -1):
            ___ j __ r..(n-1, -1, -1):
                __ matrix[i][j] __ 0:
                    continue
                __ i __ n-1 and j __ n-1:
                    dp[i][j][2] = 1
                    dp[i][j][3] = 1
                ____ i __ n-1 and j != n-1:
                    dp[i][j][2] = 1
                    dp[i][j][3] = dp[i][j+1][3]+1
                ____ i != n-1 and j __ n-1:
                    dp[i][j][2] = dp[i+1][j][2]+1
                    dp[i][j][3] = 1
                ____:
                    dp[i][j][2] = dp[i+1][j][2]+1
                    dp[i][j][3] = dp[i][j+1][3]+1
        ___ i __ r..(n):
            ___ j __ r..(n):
                maxLen = max(maxLen, m..(dp[i][j]))
        r.. maxLen
    
    ___ test(self):
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
            result = self.orderOfLargestPlusSign(n, mines)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
