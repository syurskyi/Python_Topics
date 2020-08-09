"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
______ ma__
__author__ = 'Danyang'


class Solution(object
    ___ uniquePaths(self, m, n
        """
        Math solution:
        if total m+n steps
        (m+n) \choose m as down, the remain n as right.

        mCn = n!/m!(n-m)!
        :param m:
        :param n:
        :return:
        """
        m -= 1
        n -= 1
        r_ ma__.factorial(m+n) / (ma__.factorial(n) * ma__.factorial(m))

    ___ uniquePathsDP(self, m, n
        F = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        F[1][0] = 1  # dummy entry point
        for i in xrange(1, m+1
            for j in xrange(1, n+1
                F[i][j] = F[i-1][j] + F[i][j-1]

        r_ F[m][n]

    ___ uniquePathsNormal(self, m, n
        """
        dp
        Let F be number of unique paths at position i, j
        F[i][j] = F[i-1][j] + F[i][j-1]
        :param m:
        :param n:
        :return: an integer
        """
        F = [[0 for _ in xrange(n)] for _ in xrange(m)]
        F[0][0] = 1  # start

        # F[i][j] = F[i-1][j] + F[i][j-1]
        for i in xrange(m
            for j in xrange(n
                __ i __ 0 and j __ 0: continue
                __ i __ 0: F[i][j] = F[i][j-1]
                ____ j __ 0: F[i][j] = F[i-1][j]
                ____ F[i][j] = F[i-1][j]+F[i][j-1]

        r_ F[m-1][n-1]


__ __name__ __ "__main__":
    assert Solution().uniquePaths(3, 7) __ 28