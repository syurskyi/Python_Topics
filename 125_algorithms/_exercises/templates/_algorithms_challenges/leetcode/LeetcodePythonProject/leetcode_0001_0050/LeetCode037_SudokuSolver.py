'''
Created on Oct 31, 2017

@author: MT
'''
class Solution(object
    ___ solveSudoku(self, board
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    ___ solve(self, board
        ___ i in range(9
            ___ j in range(9
                __ board[i][j] __ '.':
                    ___ c in '123456789':
                        __ self.isValid(board, i, j, c
                            board[i][j] = c
                            __ self.solve(board
                                r_ True
                            ____
                                board[i][j] = '.'
                    r_ False
        r_ True
    
    ___ isValid(self, board, row, col, c
        ___ i in range(9
            __ board[i][col] __ c: r_ False
            __ board[row][i] __ c: r_ False
            __ board[3*(row//3)+i//3][3*(col//3)+i%3] __ c:
                r_ False
        r_ True
