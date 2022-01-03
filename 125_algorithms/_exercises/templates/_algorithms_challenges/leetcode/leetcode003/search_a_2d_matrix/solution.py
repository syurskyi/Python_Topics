# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous
row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

c_ Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    ___ searchMatrix(self, matrix, target):
        row_left = 0
        row_right = l..(matrix) - 1
        w.... row_left <= row_right:
            row_mid = row_left + (row_right - row_left) / 2
            row = matrix[row_mid]
            __ target >= row[0] a.. target <= row[-1]:
                left = 0
                right = l..(row) - 1
                w.... left <= right:
                    mid = left + (right - left) / 2
                    __ target __ row[mid]:
                        r.. T..
                    ____ target < row[mid]:
                        right = mid - 1
                    ____:
                        left = mid + 1
                r.. F..
            ____ target < row[0]:
                row_right = row_mid - 1
            ____:
                row_left = row_mid + 1
        r.. F..
