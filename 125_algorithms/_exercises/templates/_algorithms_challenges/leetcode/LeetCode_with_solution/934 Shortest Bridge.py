#!/usr/bin/python3
"""
In a given 2D binary array A, there are two islands.  (An island is a
4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1
island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that
the answer is at least 1.)

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Note:
1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
____ t___ _______ L..


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


c_ Solution:
    ___ shortestBridge  A: L..[L..[i..]]) __ i..:
        """
        market component 1 and component 2
        iterate 0 and BFS, min(dist1 + dist2 - 1)?
        O(N * N) high complexity

        BFS grow from 1 component
        """
        m, n = l..(A), l..(A[0])
        # coloring
        colors = [[N.. ___ _ __ r..(n)] ___ _ __ r..(m)]
        color = 0
        ___ i __ r..(m
            ___ j __ r..(n
                __ A[i][j] __ 1 a.. colors[i][j] __ N..
                    dfs(A, i, j, colors, color)
                    color += 1
        ... color __ 2

        # BFS
        step = 0
        q    # list
        visited = [[F.. ___ _ __ r..(n)] ___ _ __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ colors[i][j] __ 0:
                    visited[i][j] = T..
                    q.a..((i, j))

        w.... q:
            cur_q    # list
            ___ i, j __ q:
                ___ I, J __ nbr(A, i, j
                    __ n.. visited[I][J]:
                        __ colors[I][J] __ N..
                            visited[I][J] = T..   # pre-check, dedup
                            cur_q.a..((I, J))
                        ____ colors[I][J] __ 1:
                            r.. step
            step += 1
            q = cur_q

        r..

    ___ nbr  A, i, j
        m, n = l..(A), l..(A[0])
        ___ di, dj __ dirs:
            I = i + di
            J = j + dj
            __ 0 <= I < m a.. 0 <= J < n:
                y.. I, J

    ___ dfs  A, i, j, colors, color
        colors[i][j] = color
        ___ I, J __ nbr(A, i, j
            __ colors[I][J] __ N.. a.. A[I][J] __ 1:
                dfs(A, I, J, colors, color)


__ _______ __ _______
    ... Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]) __ 1
