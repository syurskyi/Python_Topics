'''
Created on Sep 24, 2019

@author: tongq
'''
c_ Solution(object):
    ___ shortestPathAllKeys  grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m, n = l..(grid), l..(grid[0])
        numOfKeys = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        moves = set()
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ '@':
                    starti = i
                    startj = j
                ____ grid[i][j] __ 'abcdef':
                    numOfKeys += 1
        d..    # list
        d...a..([starti, startj, 0, '.@abcdef', 0])
        w.... d..:
            i, j, steps, keys, collectedKeys = d...pop(0)
            __ grid[i][j] __ 'abcdef' a.. grid[i][j].u.. n.. __ keys:
                keys += grid[i][j].u..
                collectedKeys += 1
            __ collectedKeys __ numOfKeys:
                r.. steps
            ___ x, y __ dirs:
                ni = i+x
                nj = j+y
                __ 0<=ni<m a.. 0<=nj<n a.. grid[ni][nj] __ keys:
                    __ (ni, nj, keys) n.. __ moves:
                        moves.add((ni, nj, keys))
                        d...a..([ni, nj, steps+1, keys, collectedKeys])
        r.. -1
    
    ___ test
        testCase = [
            
        ]
        ___ grid __ testCase:
            res = shortestPathAllKeys(grid)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
