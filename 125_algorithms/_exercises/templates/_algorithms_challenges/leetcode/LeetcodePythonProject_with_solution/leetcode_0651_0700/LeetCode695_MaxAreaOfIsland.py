'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object):
    ___ maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. 0
        m, n = l..(grid), l..(grid[0])
        maxArea = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                maxArea = max(maxArea, self.bfs(grid, m, n, i, j))
        r.. maxArea
    
    ___ bfs(self, grid, m, n, i, j):
        __ grid[i][j] __ 0:
            r.. 0
        area = 0
        grid[i][j] = -1
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            area += 1
            ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                __ 0 <= x < m and 0 <= y < n and grid[x][y] __ 1:
                    queue.a..((x, y))
                    grid[x][y] = -1
        r.. area
    
    ___ test(self):
        testCases = [
            [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
        ]
        ___ grid __ testCases:
            result = self.maxAreaOfIsland(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
