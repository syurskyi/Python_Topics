#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ longestIncreasingPath  matrix
        """
        According to:
        https://leetcode.com/discuss/81747/python-solution-memoization-dp-288ms
        1. Do DFS from every cell
        2. Compare every 4 direction and skip unmatched cells.
        3. Get matrix max from every cell's max
        4. Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
        The key is to cache the distance because it's frequently to revisit a cell
        """
        ___ dfs(i, j
            __ n.. dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + m..(
                    dfs(i - 1, j) __ i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) __ i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) __ j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) __ j < N - 1 and val > matrix[i][j + 1] else 0)
            r_ dp[i][j]

        __ n.. matrix or n.. matrix[0]:
            r_ 0
        M, N = l..(matrix), l..(matrix[0])
        dp = [[0] * N ___ i __ r..(M)]
        r_ m..(dfs(x, y) ___ x __ r..(M) ___ y __ r..(N))

"""
[[]]
[[3,4,5],[3,2,6],[2,2,1]]
[[9,9,4],[6,6,8],[2,1,1]]
"""
