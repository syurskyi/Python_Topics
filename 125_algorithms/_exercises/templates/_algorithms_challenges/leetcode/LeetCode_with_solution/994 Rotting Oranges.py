#!/usr/bin/python3
"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never
rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer
is just 0.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
____ t___ _______ L..


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0


c_ Solution:
    ___ orangesRotting  grid: L..[L..[i..]]) __ i..:
        """
        maintain a q for the newly rotten
        """
        m, n = l..(grid), l..(grid[0])
        q    # list
        ___ i __ r..(m
            ___ j __ r..(n
                __ grid[i][j] __ 2:
                    q.a..((i, j

        t = -1
        w.... q:
            t += 1
            cur_q    # list
            ___ i, j __ q:
                ___ di, dj __ dirs:
                    I = i + di
                    J = j + dj
                    __ 0 <= I < m a.. 0 <= J < n a.. grid[I][J] __ 1:
                        grid[I][J] = 2
                        cur_q.a..((I, J
            q = cur_q

        has_fresh = any(
            grid[i][j] __ 1
            ___ i __ r..(m)
            ___ j __ r..(n)
        )

        r.. m..(0, t) __ n.. has_fresh ____ -1
