#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    """
    O(m+n)
    Check the top-right corner.
    If it's not the target, then remove the top row or rightmost column.
    """
    ___ searchMatrix  matrix, target
        __ n.. matrix or l..(matrix[0]) < 1:
            r_ False
        m, n = l..(matrix), l..(matrix[0])

        # We start search the matrix from top right corner
        # Initialize the current position to top right corner.
        row, col = 0, n - 1
        _____ row < m and col >= 0:
            __ matrix[row][col] __ target:
                r_ True
            ____ matrix[row][col] > target:
                col -= 1
            ____
                row += 1
        r_ False


c.. Solution_2 o..
    # O(m+n): same as the pre solution, more efficient and pythonic.
    # According to
    # https://leetcode.com/discuss/47571/4-lines-c-6-lines-ruby-7-lines-python-1-liners
    ___ searchMatrix  matrix, target
        __ n.. matrix or l..(matrix[0]) < 1:
            r_ False
        n = l..(matrix[0])
        col = -1
        ___ row __ matrix:
            _____ col + n > 0 and row[col] > target:
                col -= 1
            __ row[col] __ target:
                r_ True
        r_ False


c.. Solution_3 o..
    # O(mn): 1 lines python. Just for fun
    ___ searchMatrix  matrix, target
        r_ any(target __ row ___ row __ matrix)

"""
[[]]
0
[[-5]]
-2
[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24]]
12
"""
