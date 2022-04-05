"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
_______ m__
__author__ = 'Danyang'


c_ Solution(o..
    ___ uniquePaths  m, n
        """
        Math solution:
        if total m+n steps
        (m+n) \choose m as down, the remain n as right.

        mCn = n!/m!(n-m)!
        :param m:
        :param n:
        :return:
        """
        m -_ 1
        n -_ 1
        r.. m__.factorial(m+n) / (m__.factorial(n) * m__.factorial(m

    ___ uniquePathsDP  m, n
        F = [[0 ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]
        F[1][0] = 1  # dummy entry point
        ___ i __ x..(1, m+1
            ___ j __ x..(1, n+1
                F[i][j] = F[i-1][j] + F[i][j-1]

        r.. F[m][n]

    ___ uniquePathsNormal  m, n
        """
        dp
        Let F be number of unique paths at position i, j
        F[i][j] = F[i-1][j] + F[i][j-1]
        :param m:
        :param n:
        :return: an integer
        """
        F = [[0 ___ _ __ x..(n)] ___ _ __ x..(m)]
        F[0][0] = 1  # start

        # F[i][j] = F[i-1][j] + F[i][j-1]
        ___ i __ x..(m
            ___ j __ x..(n
                __ i __ 0 a.. j __ 0: _____
                __ i __ 0: F[i][j] = F[i][j-1]
                ____ j __ 0: F[i][j] = F[i-1][j]
                ____ F[i][j] = F[i-1][j]+F[i][j-1]

        r.. F[m-1][n-1]


__ _______ __ _______
    ... Solution().uniquePaths(3, 7) __ 28