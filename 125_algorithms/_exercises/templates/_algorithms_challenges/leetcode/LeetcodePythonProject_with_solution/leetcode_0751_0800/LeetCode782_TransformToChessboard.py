'''
Created on Apr 9, 2018

@author: tongq
'''
c_ Solution(object):
    ___ movesToChessboard  board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = l..(board)
        rowSum, colSum, rowSwap, colSwap = 0, 0, 0, 0
        ___ i __ r..(n):
            ___ j __ r..(n):
                __ board[0][0]^board[i][0]^board[0][j]^board[i][j] __ 1:
                    r.. -1
        ___ i __ r..(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            __ board[i][0] __ i%2:
                rowSwap += 1
            __ board[0][i] __ i%2:
                colSwap += 1
        __ n//2 > rowSum o. rowSum > (n+1)//2:
            r.. -1
        __ n//2 > colSum o. colSum > (n+1)//2:
            r.. -1
        __ n % 2 __ 1:
            __ colSwap%2 __ 1:
                colSwap = n-colSwap
            __ rowSwap%2 __ 1:
                rowSwap = n-rowSwap
        ____:
            colSwap = m..(n-colSwap, colSwap)
            rowSwap = m..(n-rowSwap, rowSwap)
        r.. (colSwap+rowSwap)//2
    
    ___ test
        testCases = [
            [
                [0,1,1,0],
                [0,1,1,0],
                [1,0,0,1],
                [1,0,0,1],
            ],
            [
                [0, 1],
                [1, 0],
            ],
            [
                [1, 0],
                [1, 0],
            ],
        ]
        ___ board __ testCases:
            result = movesToChessboard(board)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
