'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object):
    ___ numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        __ n.. grid: r.. 0
        m, n = l..(grid), l..(grid[0])
        res = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ '1':
                    grid[i][j] = '#'
                    res += 1
                    self.bfs(grid, i, j)
        r.. res
    
    ___ bfs(self, grid, i, j):
        queue = [(i, j)]
        m, n = l..(grid), l..(grid[0])
        while queue:
            i, j = queue.pop(0)
            ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                __ 0 <= x < m and 0 <= y < n and grid[x][y] __ '1':
                    grid[x][y] = '#'
                    queue.a..([x, y])
    
    ___ test(self):
        testCases = [
#             [
#                 '11110',
#                 '11010',
#                 '11000',
#                 '00000',
#             ],
            [
                '11000',
                '11000',
                '00100',
                '00011',
            ],
        ]
        ___ grid __ testCases:
            grid = [l..(x) ___ x __ grid]
            result = self.numIslands(grid)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
