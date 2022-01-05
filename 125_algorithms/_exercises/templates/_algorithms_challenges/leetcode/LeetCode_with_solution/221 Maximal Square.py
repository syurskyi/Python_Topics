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


c_ Solution:
    ___ maximalSquare  matrix):
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
        m = l..(matrix)
        __ m < 1: r.. 0
        n = l..(matrix[0])
        __ n < 1: r.. 0
        ___ i __ x..(m):
            matrix[i] = map(i.., matrix[i])

        maxa = 0
        to_top = [[0 ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]
        to_left = [[0 ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]
        square_width = [[0 ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]

        ___ i __ x..(1, m+1):
            ___ j __ x..(1, n+1):
                __ matrix[i-1][j-1] __ 0:
                    _____

                to_top[i][j] += to_top[i-1][j] + matrix[i-1][j-1]
                to_left[i][j] += to_left[i][j-1] + matrix[i-1][j-1]
                square_width[i][j] = m..(
                    square_width[i-1][j-1]+1,
                    to_left[i][j],
                    to_top[i][j],
                )
                maxa = m..(maxa, square_width[i][j])

        r.. maxa*maxa

