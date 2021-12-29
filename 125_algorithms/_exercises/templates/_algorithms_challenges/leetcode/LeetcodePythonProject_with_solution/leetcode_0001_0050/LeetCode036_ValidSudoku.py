'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    ___ isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ___ i __ r..(9):
            hashset = set()
            ___ j __ r..(9):
                __ board[i][j] __ hashset:
                    r.. False
                __ board[i][j] != '.':
                    hashset.add(board[i][j])
        ___ j __ r..(9):
            hashset = set()
            ___ i __ r..(9):
                __ board[i][j] __ hashset:
                    r.. False
                __ board[i][j] != '.':
                    hashset.add(board[i][j])
        ___ i0 __ r..(3):
            ___ j0 __ r..(3):
                hashset = set()
                ___ i __ r..(i0*3, i0*3+3):
                    ___ j __ r..(j0*3, j0*3+3):
                        __ board[i][j] __ hashset:
                            r.. False
                        __ board[i][j] != '.':
                            hashset.add(board[i][j])
        r.. True
