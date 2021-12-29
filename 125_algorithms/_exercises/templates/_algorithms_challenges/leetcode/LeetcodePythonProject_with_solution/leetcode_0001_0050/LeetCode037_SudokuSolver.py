'''
Created on Oct 31, 2017

@author: MT
'''
class Solution(object):
    ___ solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    ___ solve(self, board):
        for i in range(9):
            for j in range(9):
                __ board[i][j] == '.':
                    for c in '123456789':
                        __ self.isValid(board, i, j, c):
                            board[i][j] = c
                            __ self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    ___ isValid(self, board, row, col, c):
        for i in range(9):
            __ board[i][col] == c: return False
            __ board[row][i] == c: return False
            __ board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                return False
        return True
