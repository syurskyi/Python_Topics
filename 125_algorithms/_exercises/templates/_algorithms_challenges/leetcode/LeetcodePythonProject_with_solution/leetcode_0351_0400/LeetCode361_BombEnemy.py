'''
Created on Mar 27, 2017

@author: MT
'''

c_ Solution(o..
    ___ maxKilledEnemies  grid
        __ n.. grid o. n.. grid[0]: r.. 0
        m, n = l..(grid), l..(grid[0])
        res = 0
        rows = 0
        cols = [0]*n
        ___ i __ r..(m
            ___ j __ r..(n
                __ j __ 0 o. grid[i][j-1] __ 'W':
                    rows = 0
                    ___ k __ r..(j, n
                        __ grid[i][k] __ 'W': _____
                        __ grid[i][k] __ 'E': rows += 1
                __ i __ 0 o. grid[i-1][j] __ 'W':
                    cols[j] = 0
                    ___ k __ r..(i, m
                        __ grid[k][j] __ 'W': _____
                        __ grid[k][j] __ 'E': cols[j] += 1
                __ grid[i][j] __ '0':
                    res = m..(res, cols[j]+rows)
        r.. res
