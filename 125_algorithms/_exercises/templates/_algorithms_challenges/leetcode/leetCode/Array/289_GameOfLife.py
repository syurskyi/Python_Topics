#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ gameOfLife  board
        __ n.. board:
            r_
        m_rows = l..(board)
        n_cols = l..(board[0])
        count = [[0 ___ j __ r..(n_cols)] ___ i __ r..(m_rows)]
        ___ i __ r..(m_rows
            ___ j __ r..(n_cols
                # Compute the number of live neighbors and
                # Update the count of adjancent next cells meanwhile.
                __ j+1 < n_cols:
                    count[i][j] += board[i][j+1]
                    count[i][j+1] += board[i][j]
                __ i+1 < m_rows:
                    count[i][j] += board[i+1][j]
                    count[i+1][j] += board[i][j]
                    __ j-1 >= 0:
                        count[i][j] += board[i+1][j-1]
                        count[i+1][j-1] += board[i][j]
                    __ j+1 < n_cols:
                        count[i][j] += board[i+1][j+1]
                        count[i+1][j+1] += board[i][j]
                # Current cell interacts with its eight neighbors
                # Live cell turn dead
                __ board[i][j] a.. (count[i][j] < 2 or count[i][j] > 3
                    board[i][j] = 0
                # Dead cell turn live
                __ n.. board[i][j] a.. count[i][j] __ 3:
                    board[i][j] = 1
        r_

"""
[[]]
[[0]]
[[1,1],[0,1]]
[[0,1,0],[1,1,1],[0,1,0]]
"""
