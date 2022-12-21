#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    ___ solveSudoku  board
        """ Hash and Backtracking.

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Pay Attention, can not define two-degree array as: [[0]*9]*9
        self.rows_hash, self.cols_hash = [[0] * 9 ___ i __ r..(9)], [[0] * 9 ___ i __ r..(9)]
        self.panel_hash = [[0] * 9 ___ i __ r..(9)]

        # Add all existing number to hash.
        ___ i __ xrange(9
            ___ j __ xrange(9
                __ board[i][j] != ".":
                    self.try_num(int(board[i][j]) - 1, i, j)

        self.dfs_search(0, board)

    ___ dfs_search  cur, board
        __ cur __ 81:
            r_ True
        r, c = cur / 9, cur % 9

        # The existing number must be valid, because we are promised that
        # there will be only one unique solution.
        __ board[r][c] != ".":
            r_ self.dfs_search(cur + 1, board)

        ____
            ___ n __ self.nums_list:
                __ self.try_num(n - 1, r, c
                    board[r][c] = str(n)
                    __ self.dfs_search(cur + 1, board
                        r_ True
                    # Remember to bacrtrack here.
                    board[r][c] = "."
                    self.backtrack(n - 1, r, c)
            r_ False

    ___ try_num  num, row, col
        panel_pos = row / 3 * 3 + col / 3
        __ (self.rows_hash[row][num] or self.cols_hash[col][num] or
                self.panel_hash[panel_pos][num]
            r_ False
        ____
            self.rows_hash[row][num] = 1
            self.cols_hash[col][num] = 1
            self.panel_hash[panel_pos][num] = 1
            r_ True

    ___ backtrack  num, row, col
        panel_pos = row / 3 * 3 + col / 3
        self.rows_hash[row][num] = 0
        self.cols_hash[col][num] = 0
        self.panel_hash[panel_pos][num] = 0

"""
["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
"""
