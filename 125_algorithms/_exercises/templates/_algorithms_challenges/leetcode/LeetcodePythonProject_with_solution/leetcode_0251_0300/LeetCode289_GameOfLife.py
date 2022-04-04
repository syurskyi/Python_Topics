'''
Created on Mar 7, 2017

@author: MT
'''
c_ Solution
    ___ gameOfLife  board
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 2: live => die
        # -1: die => live
        m, n = l..(board), l..(board[0])
        ___ i __ r..(m
            ___ j __ r..(n
                liveNum = liveNeighborNum(board, i, j)
                __ board[i][j] __ 1:
                    __ liveNum < 2 o. liveNum > 3:
                        board[i][j] = 2
                ____:
                    __ liveNum __ 3:
                        board[i][j] = -1
        ___ i __ r..(m
            ___ j __ r..(n
                __ board[i][j] __ 2:
                    board[i][j] = 0
                ____ board[i][j] __ -1:
                    board[i][j] = 1
    
    ___ liveNeighborNum  board, i, j
        count = 0
        ___ i0 __ r..(m..(i-1, 0), m..(l..(board), i+2:
            ___ j0 __ r..(m..(j-1, 0), m..(l..(board[0]), j+2:
                __ i0 __ i a.. j0 __ j: _____
                __ board[i0][j0] __ (1, 2
                    count+=1
        r.. count
    
    ___ test
        board = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
        ]
        print('before:')
        print('\n'.j..([s..(l) ___ l __ board]
        print('after:')
        gameOfLife(board)
        print('\n'.j..([s..(l) ___ l __ board]

__ _____ __ _____
    Solution().test()
