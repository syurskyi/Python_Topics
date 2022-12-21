#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-12 23:19:24


c.. Solution o..
    ___ rotate  matrix
        """Rotate the image by 90 degrees (clockwise).

        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        After rotate, the element in A[i][j] moves to A[j][n-1-i].  So we can
        Firstly reverse up to down : A[i][j]     --> A[n-1-i][j]
        Then then swap the symmetry: A[n-1-i][j] --> A[j][n-1-i]

        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        """
        length = l..(matrix)
        ___ i __ r..(length / 2
            matrix[i], matrix[length - 1 - i] = matrix[length - 1 - i], matrix[i]

        ___ i __ r..(length
            ___ j __ r..(i
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


c.. Solution_2 o..
    ___ rotate  matrix
        """Pythonic way which is amazing.

        According to:
        https://leetcode.com/discuss/82450/1-line-in-python
        """
        matrix[::] = zip(*matrix[::-1])

"""
[[1]]
[[1,2], [3,4]]
[[1,2,3], [4,5,6], [7,8,9]]
"""
