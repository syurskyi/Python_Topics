'''
Created on Mar 18, 2017

@author: MT
'''

c_ Solution(object):
    ___ longestIncreasingPath(self, matrix):
        __ n.. matrix: r.. 0
        m, n = l..(matrix), l..(matrix[0])
        mem = [[0]*n ___ _ __ r..(m)]
        maxPath = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                maxPath = max(maxPath, helper(matrix, i, j, mem))
        r.. maxPath
    
    ___ helper(self, matrix, i, j, mem):
        m, n = l..(matrix), l..(matrix[0])
        __ mem[i][j]:
            r.. mem[i][j]
        ___ x, y __ ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            __ 0 <= x < m a.. 0 <= y < n a.. matrix[x][y] > matrix[i][j]:
                mem[i][j] = max(mem[i][j], helper(matrix, x, y, mem))
        mem[i][j] += 1
        r.. mem[i][j]
    
    ___ test
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
        ___ matrix __ testCases:
            result = longestIncreasingPath(matrix)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
