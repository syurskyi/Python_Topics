'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object
    ___ countBattleships(self, board
        """
        :type board: List[List[str]]
        :rtype: int
        """
        __ not board or not board[0]: r_ 0
        m, n = le.(board), le.(board[0])
        count = 0
        ___ i __ range(m
            ___ j __ range(n
                __ board[i][j] __ 'X':
                    __ i __ 0:
                        __ j __ 0:
                            count += 1
                        ____ board[i][j-1] __ '.':
                            count += 1
                    ____ j __ 0:
                        __ board[i-1][j] __ '.':
                            count += 1
                    ____
                        __ board[i-1][j] __ '.' and board[i][j-1] __ '.':
                            count += 1
        r_ count
    