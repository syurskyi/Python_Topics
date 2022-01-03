#!/usr/bin/python3
"""
Given an m x n matrix of non-negative integers representing the height of each
nit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to
another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
parentheses in above matrix).
"""
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


c_ Solution:
    ___ pacificAtlantic(self, matrix):
        """
        dfs, visisted O(1)
        Similar to Trapping Rainwater II (BFS + heap), but no need to record
        volume, thus, dfs is enough.

        Similar to longest increasing path

        Starting from the edge point rather than any point, dfs visit the
        possible cell

        Complexity analysis, although a cell can be checked multiple times
        (at most 4 times); but only perform 1 dfs on each cell; thus
        O(mn)

        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. []

        m, n = l..(matrix), l..(matrix[0])  # row, col
        # don't do [[False] * n ] * m, memory management, all rows reference the same row
        P = [[F.. ___ _ __ r..(n)] ___ _ __ r..(m)]
        A = [[F.. ___ _ __ r..(n)] ___ _ __ r..(m)]

        # starting from edge point
        ___ i __ r..(m):
            dfs(matrix, i, 0, P)
            dfs(matrix, i, n-1, A)

        ___ j __ r..(n):
            dfs(matrix, 0, j, P)
            dfs(matrix, m-1, j, A)

        ret = [
            [i, j]
            ___ i __ r..(m)
            ___ j __ r..(n)
            __ P[i][j] a.. A[i][j]
        ]
        r.. ret

    ___ dfs(self, matrix, i, j, C):
        # check before dfs (to be consistent)
        C[i][j] = T..
        m, n = l..(matrix), l..(matrix[0])
        ___ x, y __ dirs:
            I = i + x
            J = j + y
            __ 0 <= I < m a.. 0 <= J < n a.. matrix[i][j] <= matrix[I][J]:
                __ n.. C[I][J]:
                    dfs(matrix, I, J, C)


    ___ pacificAtlantic_error(self, matrix):
        """
        DP
        dfs, visisted O(1)
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. []

        m, n = l..(matrix), l..(matrix[0])  # row, col
        P = [[F..] * n ] * m
        A = [[F..] * n ] * m

        visisted = [[F..] * n ] * m
        ___ i __ r..(m):
            ___ j __ r..(n):
                dfs_error(matrix, i, j, visisted, P, l.... i, j: i < 0 o. j <0)

        visisted = [[F..] * n ] * m
        ___ i __ r..(m):
            ___ j __ r..(n):
                dfs_error(matrix, i, j, visisted, A, l.... i, j: i >= m o. j >= n)

        ret = [
            [i, j]
            ___ i __ r..(m)
            ___ j __ r..(n)
            __ P[i][j] a.. A[i][j]
        ]
        r.. ret


    ___ dfs_error(self, matrix, i, j, visisted, C, predicate):
        m, n = l..(matrix), l..(matrix[0])
        __ visisted[i][j]:
            r.. C[i][j]

        visisted[i][j] = T..
        ___ x, y __ dirs:
            i2 = i + x
            j2= j + y
            __ 0 <= i2 < m a.. 0 <= j2 < n:
                __ dfs_error(matrix, i2, j2, visisted, C, predicate) a.. matrix[i][j] >= matrix[i2][j2]:
                    C[i][j] = T..
            ____ predicate(i2, j2):
                C[i][j] = T..

        r.. C[i][j]


__ __name__ __ "__main__":
    ... Solution().pacificAtlantic([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]) __ [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
