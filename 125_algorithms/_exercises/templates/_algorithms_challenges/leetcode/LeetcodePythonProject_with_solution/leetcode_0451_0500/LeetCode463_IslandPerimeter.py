'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    ___ islandPerimeter(self, grid):
        result = 0
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    result += self.getParameter(i, j, grid)
        r.. result
    
    ___ getParameter(self, i, j, grid):
        m, n = l..(grid), l..(grid[0])
        p = 4
        ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            __ 0 <= x < m and 0 <= y < n and grid[x][y] __ 1:
                p -= 1
        r.. p
