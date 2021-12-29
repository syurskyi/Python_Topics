'''
Created on Mar 27, 2017

@author: MT
'''

class Solution(object):
    ___ maxKilledEnemies(self, grid):
        __ not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        rows = 0
        cols = [0]*n
        for i in range(m):
            for j in range(n):
                __ j == 0 or grid[i][j-1] == 'W':
                    rows = 0
                    for k in range(j, n):
                        __ grid[i][k] == 'W': break
                        __ grid[i][k] == 'E': rows += 1
                __ i == 0 or grid[i-1][j] == 'W':
                    cols[j] = 0
                    for k in range(i, m):
                        __ grid[k][j] == 'W': break
                        __ grid[k][j] == 'E': cols[j] += 1
                __ grid[i][j] == '0':
                    res = max(res, cols[j]+rows)
        return res
