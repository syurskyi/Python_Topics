'''
Created on Mar 27, 2017

@author: MT
'''

class Solution(object
    ___ maxKilledEnemies(self, grid
        __ not grid or not grid[0]: r_ 0
        m, n = le.(grid), le.(grid[0])
        res = 0
        rows = 0
        cols = [0]*n
        for i in range(m
            for j in range(n
                __ j __ 0 or grid[i][j-1] __ 'W':
                    rows = 0
                    for k in range(j, n
                        __ grid[i][k] __ 'W': break
                        __ grid[i][k] __ 'E': rows += 1
                __ i __ 0 or grid[i-1][j] __ 'W':
                    cols[j] = 0
                    for k in range(i, m
                        __ grid[k][j] __ 'W': break
                        __ grid[k][j] __ 'E': cols[j] += 1
                __ grid[i][j] __ '0':
                    res = max(res, cols[j]+rows)
        r_ res
