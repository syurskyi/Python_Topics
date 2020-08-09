"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
__author__ = 'Daniel'


class Solution:
    ___ maximalSquare(self, matrix
        """
        Brute force: O(n^3)
        DP: O(n^2)
        square_width[i][j] = min(
                    square_width[i-1][j-1]+1,
                    to_left[i][j],
                    to_top[i][j],
                )

        :param matrix: matrix
        :return: int
        """
        m = le.(matrix)
        __ m < 1: r_ 0
        n = le.(matrix[0])
        __ n < 1: r_ 0
        ___ i in xrange(m
            matrix[i] = map(int, matrix[i])

        maxa = 0
        to_top = [[0 ___ _ in xrange(n+1)] ___ _ in xrange(m+1)]
        to_left = [[0 ___ _ in xrange(n+1)] ___ _ in xrange(m+1)]
        square_width = [[0 ___ _ in xrange(n+1)] ___ _ in xrange(m+1)]

        ___ i in xrange(1, m+1
            ___ j in xrange(1, n+1
                __ matrix[i-1][j-1] __ 0:
                    continue

                to_top[i][j] += to_top[i-1][j] + matrix[i-1][j-1]
                to_left[i][j] += to_left[i][j-1] + matrix[i-1][j-1]
                square_width[i][j] = min(
                    square_width[i-1][j-1]+1,
                    to_left[i][j],
                    to_top[i][j],
                )
                maxa = max(maxa, square_width[i][j])

        r_ maxa*maxa

