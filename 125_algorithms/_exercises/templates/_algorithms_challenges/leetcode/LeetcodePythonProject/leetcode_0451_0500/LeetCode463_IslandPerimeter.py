'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object
    ___ islandPerimeter(self, grid
        result = 0
        m, n = le.(grid), le.(grid[0])
        ___ i in range(m
            ___ j in range(n
                __ grid[i][j] __ 1:
                    result += self.getParameter(i, j, grid)
        r_ result
    
    ___ getParameter(self, i, j, grid
        m, n = le.(grid), le.(grid[0])
        p = 4
        ___ x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1
            __ 0 <= x < m and 0 <= y < n and grid[x][y] __ 1:
                p -= 1
        r_ p
