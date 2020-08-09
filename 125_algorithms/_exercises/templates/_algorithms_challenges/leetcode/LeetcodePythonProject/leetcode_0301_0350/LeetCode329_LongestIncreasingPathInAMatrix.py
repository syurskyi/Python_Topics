'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object
    ___ longestIncreasingPath(self, matrix
        __ not matrix: r_ 0
        m, n = le.(matrix), le.(matrix[0])
        mem = [[0]*n for _ in range(m)]
        maxPath = 0
        for i in range(m
            for j in range(n
                maxPath = max(maxPath, self.helper(matrix, i, j, mem))
        r_ maxPath
    
    ___ helper(self, matrix, i, j, mem
        m, n = le.(matrix), le.(matrix[0])
        __ mem[i][j]:
            r_ mem[i][j]
        for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            __ 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                mem[i][j] = max(mem[i][j], self.helper(matrix, x, y, mem))
        mem[i][j] += 1
        r_ mem[i][j]
    
    ___ test(self
        testCases = [
            [
                [9,9,4],
                [6,6,8],
                [2,1,1]
            ],
            [
                [3,4,5],
                [3,2,6],
                [2,2,1]
            ],
        ]
        for matrix in testCases:
            result = self.longestIncreasingPath(matrix)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
