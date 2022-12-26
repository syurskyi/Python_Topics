#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    countNQueens = 0

    ___ totalNQueens  n
        self.countNQueens = 0
        cols_used = [-1 ___ i __ r..(n)]
        self.solveNQueens(0, cols_used, n)
        r_ self.countNQueens

    ___ solveNQueens  row, cols_used, n
        ___ col __ r..(n
            __ self.isValid(row, col, cols_used, n
                __ row __ n - 1:
                    self.countNQueens += 1
                    r_

                cols_used[row] = col
                self.solveNQueens(row + 1, cols_used, n)
                cols_used[row] = -1

    ___ isValid  row, col, cols_used, n
        """ Can check isvalid with using hash, implemented by c++.

        Refer to:
        https://discuss.leetcode.com/topic/13617/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand
        The number of columns is n, the number of 45° diagonals is 2 * n - 1,
        the number of 135° diagonals is also 2 * n - 1.
        When reach [row, col], the column No. is col,
        the 45° diagonal No. is row + col and the 135° diagonal No. is n - 1 + col - row.

        | | |                / / /             \ \ \
        O O O               O O O               O O O
        | | |              / / / /             \ \ \ \
        O O O               O O O               O O O
        | | |              / / / /             \ \ \ \
        O O O               O O O               O O O
        | | |              / / /                 \ \ \
        3 columns        5 45° diagonals     5 135° diagonals    (when n is 3)
        """
        ___ i __ r..(row
            # Check for the according col above the current row.
            __ cols_used[i] __ col:
                r_ F..

            # Check from left-top to right-bottom
            __ cols_used[i] __ col - row + i:
                r_ F..

            # Check from right-top to left-bottom
            __ cols_used[i] __ col + row - i:
                r_ F..
        r_ True

"""
1
5
8
"""
