'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object
    ___ isValidSudoku(self, board
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ___ i in range(9
            hashset = set()
            ___ j in range(9
                __ board[i][j] in hashset:
                    r_ False
                __ board[i][j] != '.':
                    hashset.add(board[i][j])
        ___ j in range(9
            hashset = set()
            ___ i in range(9
                __ board[i][j] in hashset:
                    r_ False
                __ board[i][j] != '.':
                    hashset.add(board[i][j])
        ___ i0 in range(3
            ___ j0 in range(3
                hashset = set()
                ___ i in range(i0*3, i0*3+3
                    ___ j in range(j0*3, j0*3+3
                        __ board[i][j] in hashset:
                            r_ False
                        __ board[i][j] != '.':
                            hashset.add(board[i][j])
        r_ True
