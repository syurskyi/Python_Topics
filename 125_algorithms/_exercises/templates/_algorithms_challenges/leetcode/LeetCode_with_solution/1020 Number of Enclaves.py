#!/usr/bin/python3
"""
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land
square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the
boundary of the grid in any number of moves.

Example 1:
Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation:
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed
because its on the boundary.

Example 2:
Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation:
All 1s are either on the boundary or can reach the boundary.

Note:
1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""
____ t___ _______ L..


dirs ((0, -1), (0, 1), (1, 0), (-1, 0


c_ Solution:
    ___ numEnclaves  A: L..[L..[i..]]) __ i..:
        """
        not dfs from any cell, but dfs from the edges
        """
        m, n l..(A), l..(A[0])
        visited [[F.. ___ _ __ r..(n)] ___ _ __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ n.. visited[i][j] a.. A[i][j] __ 1 a.. (i __ 0 o. j __ 0 o. i __ m - 1 o. j __ n - 1
                    dfs(A, i, j, visited)

        ret 0
        ___ i __ r..(m
            ___ j __ r..(n
                __ A[i][j] __ 1 a.. n.. visited[i][j]:
                    ret += 1
        r.. ret

    ___ dfs  A, i, j, visited
        m, n l..(A), l..(A[0])
        visited[i][j] T..
        ___ di, dj __ dirs:
            I i + di
            J j + dj
            __ 0 <_ I < m a.. 0 <_ J < n a.. n.. visited[I][J] a.. A[I][J] __ 1:
                dfs(A, I, J, visited)


c_ SolutionError:
    ___ -
        ret 0

    ___ numEnclaves  A: L..[L..[i..]]) __ i..:
        """
        dfs coloring
        """
        m, n l..(A), l..(A[0])
        visited [[N.. ___ _ __ r..(n)] ___ _ __ r..(m)]  # 0 not off, 1 off
        ___ i __ r..(m
            ___ j __ r..(n
                __ n.. visited[i][j] a.. A[i][j] __ 1:
                    dfs(A, i, j, visited)
        r.. ret

    ___ dfs  A, i, j, visited
        m, n l..(A), l..(A[0])
        visited[i][j] 0
        ___ di, dj __ dirs:
            I i + di
            J j + dj
            __ n.. (0 <_ I < m a.. 0 <_ J < n
                visited[i][j] 1
                r.. T..
            __ visited[I][J] __ 1:
                visited[i][j] 1
                r.. T..
            __ visited[I][J] __ N.. a.. A[I][J] __ 1 a.. dfs(A, I, J, visited
                visited[i][j] 1
                r.. T..

        ret += 1
        r.. F..
