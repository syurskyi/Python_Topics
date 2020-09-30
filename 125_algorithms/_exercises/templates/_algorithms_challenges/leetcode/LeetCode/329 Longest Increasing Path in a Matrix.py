"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move
outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        self.cache = None
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    ___ longestIncreasingPath(self, matrix
        """
        dfs + cache
        :type matrix: List[List[int]]
        :rtype: int
        """
        __ not matrix: r_ 0

        m, n = le.(matrix), le.(matrix[0])
        self.cache = [[None ___ _ __ xrange(n)] ___ _ __ xrange(m)]
        gmax = 1
        ___ i __ xrange(m
            ___ j __ xrange(n
                gmax = ma.(gmax, self.longest(matrix, i, j))

        r_ gmax

    ___ longest(self, matrix, i, j
        """
        Strictly increasing, thus no need to have a visited matrix
        """
        __ not self.cache[i][j]:
            m, n = le.(matrix), le.(matrix[0])
            maxa = 1
            ___ d __ self.dirs:
                I, J = i + d[0], j + d[1]
                __ 0 <= I < m and 0 <= J < n and matrix[I][J] > matrix[i][j]:
                    maxa = ma.(maxa, 1 + self.longest(matrix, I, J))

            self.cache[i][j] = maxa

        r_ self.cache[i][j]


__  -n __ "__main__":
    assert Solution().longestIncreasingPath([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]) __ 4
