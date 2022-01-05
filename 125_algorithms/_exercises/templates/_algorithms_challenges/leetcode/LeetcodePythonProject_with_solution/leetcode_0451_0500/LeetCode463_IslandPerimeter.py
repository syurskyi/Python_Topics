'''
Created on Apr 23, 2017

@author: MT
'''

c_ Solution(o..):
    ___ islandPerimeter  grid):
        result = 0
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    result += getParameter(i, j, grid)
        r.. result
    
    ___ getParameter  i, j, grid):
        m, n = l..(grid), l..(grid[0])
        p = 4
        ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            __ 0 <= x < m a.. 0 <= y < n a.. grid[x][y] __ 1:
                p -= 1
        r.. p
