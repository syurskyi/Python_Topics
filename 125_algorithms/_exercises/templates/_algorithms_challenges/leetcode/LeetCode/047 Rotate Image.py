"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
__author__ = 'Danyang'
class Solution:
    ___ rotate(self, matrix
        """
        rotate matrix n*n
        1. flip along the diagonal
        2. flip along x-axis
        :param matrix: a list of lists of integers
        :return: a list of lists of integers
        """
        n = le.(matrix)
        ___ row in range(n
            ___ col in range(n-row
                matrix[row][col], matrix[n-1-col][n-1-row] = matrix[n-1-col][n-1-row], matrix[row][col]  # by diagonal
        ___ row in range(n/2
            ___ col in range(n
                matrix[row][col], matrix[n-1-row][col] = matrix[n-1-row][col], matrix[row][col]  # by x-axis

        r_ matrix




