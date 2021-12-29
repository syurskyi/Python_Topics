'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object):
    ___ countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        __ not board or not board[0]: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                __ board[i][j] == 'X':
                    __ i == 0:
                        __ j == 0:
                            count += 1
                        elif board[i][j-1] == '.':
                            count += 1
                    elif j == 0:
                        __ board[i-1][j] == '.':
                            count += 1
                    else:
                        __ board[i-1][j] == '.' and board[i][j-1] == '.':
                            count += 1
        return count
    