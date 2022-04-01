'''
Created on May 5, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ largestIsland  grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = l..(grid)
        index = 3
        res = 0
        areaMap    # dict
        ___ i __ r..(n):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    areaMap[index] = dfs(grid, i, j, index)
                    res = m..(res, areaMap[index])
                    index += 1
        ___ i __ r..(n):
            ___ j __ r..(n):
                __ grid[i][j] __ 0:
                    visited = s..()
                    curr = 1
                    ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                        __ 0 <= x < n a.. 0 <= y < n:
                            index = grid[x][y]
                            __ index > 1 a.. index n.. __ visited:
                                visited.add(index)
                                curr += areaMap[index]
                    res = m..(res, curr)
        r.. res
    
    ___ dfs  grid, i, j, index):
        area = 0
        n = l..(grid)
        grid[i][j] = index
        ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            __ 0 <= x < n a.. 0 <= y < n a.. grid[x][y] __ 1:
                area += dfs(grid, x, y, index)
        r.. area+1
