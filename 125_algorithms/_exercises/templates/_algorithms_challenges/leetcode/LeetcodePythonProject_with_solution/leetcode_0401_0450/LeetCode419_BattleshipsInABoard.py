'''
Created on Apr 12, 2017

@author: MT
'''

c_ Solution(object):
    ___ countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        __ n.. board o. n.. board[0]: r.. 0
        m, n = l..(board), l..(board[0])
        count = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ board[i][j] __ 'X':
                    __ i __ 0:
                        __ j __ 0:
                            count += 1
                        ____ board[i][j-1] __ '.':
                            count += 1
                    ____ j __ 0:
                        __ board[i-1][j] __ '.':
                            count += 1
                    ____:
                        __ board[i-1][j] __ '.' a.. board[i][j-1] __ '.':
                            count += 1
        r.. count
    