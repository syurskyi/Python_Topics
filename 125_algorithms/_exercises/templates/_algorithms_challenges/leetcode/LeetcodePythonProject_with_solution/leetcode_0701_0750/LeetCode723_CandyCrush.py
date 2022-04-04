'''
Created on Feb 20, 2018

@author: tongq
'''
c_ Solution(o..
    ___ candyCrush  board
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = l..(board), l..(board[0])
        res = [[0]*n ___ _ __ r..(m)]
        w... T...
            changed = F..
            ___ i __ r..(m
                ___ j __ r..(n
                    changed = bfs(board, i, j) o. changed
            __ n.. changed:
                res = board
                _____
            convert(res, board)
            board = res
        r.. res
    
    ___ bfs  board, i, j
        __ board[i][j] __ 0: r.. F..
        m, n = l..(board), l..(board[0])
        val = abs(board[i][j])
        changed = F..
        __ i+2 < m a.. val __ abs(board[i+1][j]) __ abs(board[i+2][j]
            ___ i0 __ r..(i+1, m
                __ abs(board[i0][j]) __ val:
                    board[i0][j] = -val
                ____:
                    _____
            changed = T..
        __ j+2 < n a.. val __ abs(board[i][j+1]) __ abs(board[i][j+2]
            ___ j0 __ r..(j+1, n
                __ abs(board[i][j0]) __ val:
                    board[i][j0] = -val
                ____:
                    _____
            changed = T..
        __ changed:
            board[i][j] = -val
        r.. changed
    
    ___ convert  res, board
        m, n = l..(res), l..(res[0])
        ___ j __ r..(n
            i0 = m-1
            ___ i __ r..(m-1, -1, -1
                __ board[i][j] > 0:
                    res[i0][j] = board[i][j]
                    i0 -= 1
            ___ i __ r..(i0, -1, -1
                res[i][j] = 0
    
    ___ test
        testCases = [
            [
                [110,5,112,113,114],
                [210,211,5,213,214],
                [310,311,3,313,314],
                [410,411,412,5,414],
                [5,1,512,3,3],
                [610,4,1,613,614],
                [710,1,2,713,714],
                [810,1,2,1,1],
                [1,1,2,2,2],
                [4,1,4,4,1014],
            ],
            [
                [4,5,5,4,5],[5,1,4,2,5],[4,3,1,2,2],[4,5,4,4,5],[3,3,1,1,3],
            ],
        ]
        ___ board __ testCases:
            print('board:')
            print('\n'.j..([s..(row) ___ row __ board]
            result = candyCrush(board)
            print('result:')
            print('\n'.j..([s..(row) ___ row __ result]
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
