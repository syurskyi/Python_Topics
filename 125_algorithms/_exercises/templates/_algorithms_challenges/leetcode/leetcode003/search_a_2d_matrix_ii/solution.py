# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

c_ Solution(o..
    ___ searchMatrix  matrix, target
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n l..(matrix)
        m l..(matrix[0])
        __ target < matrix[0][0] o. target > matrix[n - 1][m - 1]:
            r.. F..
        # Step-wise Linear Search from upper right
        y 0
        x m - 1
        w.... x >_ 0 a.. y <_ n - 1:
            __ target __ matrix[y][x]:
                r.. T..
            ____ target < matrix[y][x]:
                x -_ 1
            ____
                y += 1
        r.. F..


a1 [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

s Solution()
print(s.searchMatrix(a1, 5
print(s.searchMatrix(a1, 20
print(s.searchMatrix(a1, 17
