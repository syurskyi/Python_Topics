'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object
    ___ largestIsland(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = le.(grid)
        index = 3
        res = 0
        areaMap = {}
        for i in range(n
            for j in range(n
                __ grid[i][j] __ 1:
                    areaMap[index] = self.dfs(grid, i, j, index)
                    res = max(res, areaMap[index])
                    index += 1
        for i in range(n
            for j in range(n
                __ grid[i][j] __ 0:
                    visited = set()
                    curr = 1
                    for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1
                        __ 0 <= x < n and 0 <= y < n:
                            index = grid[x][y]
                            __ index > 1 and index not in visited:
                                visited.add(index)
                                curr += areaMap[index]
                    res = max(res, curr)
        r_ res
    
    ___ dfs(self, grid, i, j, index
        area = 0
        n = le.(grid)
        grid[i][j] = index
        for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1
            __ 0 <= x < n and 0 <= y < n and grid[x][y] __ 1:
                area += self.dfs(grid, x, y, index)
        r_ area+1
