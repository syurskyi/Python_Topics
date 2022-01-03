'''
Created on Oct 25, 2017

@author: MT
'''
c_ Solution(object):
    ___ numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = set()
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    island = set()
                    dfs(i, j, i, j, m, n, grid, island)
                    islands.add(tuple(island))
        r.. l..(islands)
    
    ___ dfs(self, i0, j0, i, j, m, n, grid, island):
        __ i >= m o. i < 0 o. j >= n o. j < 0 o. grid[i][j] != 1:
            r..
        grid[i][j] = -1
        island.add((i-i0, j-j0))
        ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            dfs(i0, j0, x, y, m, n, grid, island)
    
    ___ test
        testCases = [
#             [
#                 '11000',
#                 '11000',
#                 '00011',
#                 '00011',
#             ],
#             [
#                 '11011',
#                 '10000',
#                 '00001',
#                 '11011',
#             ],
            [
                [1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0],
                [1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1],
                [0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0],
                [1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1],
                [1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1],
                [0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0],
                [0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0],
                [0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1],
                [0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1],
                [0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1],
                [0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0],
                [1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1],
                [1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1],
                [0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0],
                [0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0],
                [1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0],
                [1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
                [0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0],
                [0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1],
                [0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0],
                [0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1],
                [1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0],
                [0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1],
                [1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1],
                [0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
                [1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1],
                [1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0],
                [0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0],
                [1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1],
                [0,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1],[0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,1],[0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1],[0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1],[1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1],[0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0],[0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1],[0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1],[1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1],[0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1],[1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1],[0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0],[0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1],[0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0],[0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],[1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1],[0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],[1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0],
                [0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0]
            ]
        ]
        ___ grid __ testCases:
            print('grid:')
#             print('\n'.join(grid))
            grid = [[int(c) ___ c __ row ] ___ row __ grid]
            result = numDistinctIslands(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
