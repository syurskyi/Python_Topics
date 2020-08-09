'''
Created on Mar 7, 2017

@author: MT
'''
class Solution(
    ___ gameOfLife(self, board
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 2: live => die
        # -1: die => live
        m, n = le.(board), le.(board[0])
        for i in range(m
            for j in range(n
                liveNum = self.liveNeighborNum(board, i, j)
                __ board[i][j] __ 1:
                    __ liveNum < 2 or liveNum > 3:
                        board[i][j] = 2
                ____
                    __ liveNum __ 3:
                        board[i][j] = -1
        for i in range(m
            for j in range(n
                __ board[i][j] __ 2:
                    board[i][j] = 0
                ____ board[i][j] __ -1:
                    board[i][j] = 1
    
    ___ liveNeighborNum(self, board, i, j
        count = 0
        for i0 in range(max(i-1, 0), min(le.(board), i+2)):
            for j0 in range(max(j-1, 0), min(le.(board[0]), j+2)):
                __ i0 __ i and j0 __ j: continue
                __ board[i0][j0] in (1, 2
                    count+=1
        r_ count
    
    ___ test(self
        board = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
        ]
        print('before:')
        print('\n'.join([str(l) for l in board]))
        print('after:')
        self.gameOfLife(board)
        print('\n'.join([str(l) for l in board]))

__ __name__ __ '__main__':
    Solution().test()
