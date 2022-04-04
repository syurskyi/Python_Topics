'''
Created on Apr 21, 2018

@author: tongq
'''
c_ Solution(o..
    ___ hitBricks  grid, hits
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = l..(grid), l..(grid[0])
        
        ___ dfs(i, j
            __ n.. (0<_i<m a.. 0<_j<n) o. grid[i][j]!=1:
                r.. 0
            res = 1
            grid[i][j] = 2
            res += s..(dfs(x, y) ___ x, y __ [(i-1, j), (i, j-1), (i+1, j), (i, j+1)])
            r.. res
        
        # Check whether (i, j) is connected to Not Failling Bricks
        ___ is_connected(i, j
            r.. i__0 o. any([0<_x<m a.. 0<_y<n a.. grid[x][y]__2\
                                ___ x, y __ [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]])
        
        # Mark whether there is a brick at the each hit
        ___ i, j __ hits:
            grid[i][j] -= 1
        
        # Get grid after all hits
        ___ i __ r..(n
            dfs(0, i)
        
        # Reversely and the block of each hits and get count of newly add bricks
        res = [0]*l..(hits)
        ___ k __ r..(r..(l..(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            __ grid[i][j] __ 1 a.. is_connected(i, j
                res[k] = dfs(i, j)-1
        r.. res
    
    ___ test
        testCases = [
            [
                [
                    [1,0,0,0],
                    [1,1,1,0]
                ],
                [[1,0]],
            ],
            [
                [
                    [1,0,0,0],
                    [1,1,0,0]
                ],
                [[1,1],[1,0]],
            ],
        ]
        ___ grid, hits __ testCases:
            print('grid: %s' % grid)
            print('hits: %s' % hits)
            result = hitBricks(grid, hits)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
