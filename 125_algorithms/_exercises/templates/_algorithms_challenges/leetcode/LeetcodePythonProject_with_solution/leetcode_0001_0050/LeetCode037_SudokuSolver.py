'''
Created on Oct 31, 2017

@author: MT
'''
c_ Solution(o..
    ___ solveSudoku  board
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        solve(board)
    
    ___ solve  board
        ___ i __ r..(9
            ___ j __ r..(9
                __ board[i][j] __ '.':
                    ___ c __ '123456789':
                        __ isValid(board, i, j, c
                            board[i][j] c
                            __ solve(board
                                r.. T..
                            ____
                                board[i][j] '.'
                    r.. F..
        r.. T..
    
    ___ isValid  board, row, col, c
        ___ i __ r..(9
            __ board[i][col] __ c: r.. F..
            __ board[row][i] __ c: r.. F..
            __ board[3*(row//3)+i//3][3*(col//3)+i%3] __ c:
                r.. F..
        r.. T..
