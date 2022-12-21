#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. NumMatrix o..
    # A concise explanation can be found here.
    # https://leetcode.com/discuss/69424/clean-c-solution-and-explaination-o-mn-space-with-o-1-time
    ___ __init__  matrix
        self.dp   # list
        __ n.. matrix:
            r_
        m_rows = l..(matrix)
        n_cols = l..(matrix[0])
        self.dp = [[0 ___ j __ r..(n_cols+1)] ___ i __ r..(m_rows+1)]
        # Initinal operator
        ___ m __ xrange(m_rows
            ___ n __ xrange(n_cols
                self.dp[m][n] = (self.dp[m - 1][n] + self.dp[m][n - 1] -
                                 self.dp[m - 1][n - 1] + matrix[m][n])

    ___ sumRegion  row1, col1, row2, col2
        __ n.. self.dp:
            r_ 0
        # sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        r_ (self.dp[row2][col2] - self.dp[row1-1][col2] -
                self.dp[row2][col1-1] + self.dp[row1-1][col1-1])

"""
# Your NumMatrix object will be instantiated and called as such:
if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    print numMatrix.sumRegion(2, 1, 4, 3)
    print numMatrix.sumRegion(1, 1, 2, 2)
    print numMatrix.sumRegion(1, 2, 2, 4)
"""
