'''
Created on Mar 7, 2017

@author: MT
'''
class Solution():
    ___ gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 2: live => die
        # -1: die => live
        m, n = l..(board), l..(board[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                liveNum = self.liveNeighborNum(board, i, j)
                __ board[i][j] __ 1:
                    __ liveNum < 2 o. liveNum > 3:
                        board[i][j] = 2
                ____:
                    __ liveNum __ 3:
                        board[i][j] = -1
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ board[i][j] __ 2:
                    board[i][j] = 0
                ____ board[i][j] __ -1:
                    board[i][j] = 1
    
    ___ liveNeighborNum(self, board, i, j):
        count = 0
        ___ i0 __ r..(max(i-1, 0), m..(l..(board), i+2)):
            ___ j0 __ r..(max(j-1, 0), m..(l..(board[0]), j+2)):
                __ i0 __ i a.. j0 __ j: continue
                __ board[i0][j0] __ (1, 2):
                    count+=1
        r.. count
    
    ___ test(self):
        board = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
        ]
        print('before:')
        print('\n'.join([s..(l) ___ l __ board]))
        print('after:')
        self.gameOfLife(board)
        print('\n'.join([s..(l) ___ l __ board]))

__ __name__ __ '__main__':
    Solution().test()
