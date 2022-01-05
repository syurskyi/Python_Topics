# -*- coding: utf-8 -*-
"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1,
col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains
sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
__author__ = 'Daniel'


c_ NumMatrix(object):
    ___ - , matrix):
        """
        initialize your data structure here.
        dp F[i][j] = F[i-1][j]+F[i][j-1]-F[i-1][j-1]+mat[i][j]
        :type matrix: List[List[int]]
        """
        m = l..(matrix)
        __ m __ 0:
            F = N..
            r..

        n = l..(matrix[0])
        F = [[0 ___ _ __ xrange(n+1)] ___ _ __ xrange(m+1)]
        ___ i __ xrange(1, m+1):
            ___ j __ xrange(1, n+1):
                F[i][j] = F[i-1][j]+F[i][j-1]-F[i-1][j-1]+matrix[i-1][j-1]

    ___ sumRegion  row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        """
        __ n.. F:
            r.. 0

        r.. F[row2+1][col2+1] - F[row2+1][col1] - F[row1][col2+1] + F[row1][col1]