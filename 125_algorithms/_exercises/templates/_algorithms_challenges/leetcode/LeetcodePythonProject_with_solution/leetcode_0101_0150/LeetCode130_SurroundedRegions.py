'''
Created on Feb 8, 2017

@author: MT
'''
c_ Solution(o..
    ___ solve  board
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ n.. board o. l..(board) <_ 1 o. l..(board[0]) <_ 1: r..
        m, n l..(board), l..(board[0])
        ___ i __ r..(m
            __ board[i][0] __ 'O':
                bfs(board, i, 0)
            __ board[i][n-1] __ 'O':
                bfs(board, i, n-1)
        ___ i __ r..(n
            __ board[0][i] __ 'O':
                bfs(board, 0, i)
            __ board[m-1][i] __ 'O':
                bfs(board, m-1, i)
        ___ i __ r..(m
            ___ j __ r..(n
                __ board[i][j] __ 'O':
                    board[i][j] 'X'
                __ board[i][j] __ '#':
                    board[i][j] 'O'
    
    ___ bfs  board, x, y
        board[x][y] '#'
        m, n l..(board), l..(board[0])
        index x*n+y
        queue [index]
        w.... queue:
            nextInd queue.p.. 0)
            i i..(nextInd/n)
            j nextInd%n
            __ i > 1 a.. board[i-1][j] __ 'O':
                board[i-1][j] '#'
                queue.a..((i-1)*n+j)
            __ j > 1 a.. board[i][j-1] __ 'O':
                board[i][j-1] '#'
                queue.a..(i*n+j-1)
            __ i+1 < m a.. board[i+1][j] __ 'O':
                board[i+1][j] '#'
                queue.a..((i+1)*n+j)
            __ j+1 < n a.. board[i][j+1] __ 'O':
                board[i][j+1] '#'
                queue.a..(i*n+j+1)
    
    ___ test
        testCases [
            [
                'XXXX',
                'XOOX',
                'XXOX',
                'XOXX',
            ],
        ]
        ___ matrix __ testCases:
            board [l..(l) ___ l __ matrix]
            print('before')
            print('%s' % (board
            solve(board)
            print('after')
            print('%s' % (board
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()