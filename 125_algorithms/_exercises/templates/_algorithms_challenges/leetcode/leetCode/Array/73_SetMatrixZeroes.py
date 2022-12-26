#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ setZeroes  matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        __ n.. ?
            r_ # list

        m _ l.. ?
        n _ l.. ? 0

        # Frist, make sure whether first row and first col is all 0.
        first_row _ F..
        ___ i __ r.. ?
            __ m..|0|? __ 0
                first_row = True
        first_col = F..
        ___ j __ r..(m
            __ matrix[j][0] __ 0:
                first_col = True

        # Keep the information about the 0 cell to first row and first col.
        ___ row __ r..(1, m
            ___ col __ r..(1, n
                __ matrix[row][col] __ 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Set 0s according to the information in first row and first col
        ___ row __ r..(m
            ___ col __ r..(n
                __ n.. matrix[row][0] or n.. matrix[0][col]:
                    matrix[row][col] = 0

        # Set the first row and first col
        __ first_row:
            ___ col __ r..(n
                matrix[0][col] = 0
        __ first_col:
            ___ row __ r..(m
                matrix[row][0] = 0

"""
[[0]]
[[1,0],[2,2]]
[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
"""
