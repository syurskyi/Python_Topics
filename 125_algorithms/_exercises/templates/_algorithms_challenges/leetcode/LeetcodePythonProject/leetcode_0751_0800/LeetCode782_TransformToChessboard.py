'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object
    ___ movesToChessboard(self, board
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = le.(board)
        rowSum, colSum, rowSwap, colSwap = 0, 0, 0, 0
        ___ i in range(n
            ___ j in range(n
                __ board[0][0]^board[i][0]^board[0][j]^board[i][j] __ 1:
                    r_ -1
        ___ i in range(n
            rowSum += board[0][i]
            colSum += board[i][0]
            __ board[i][0] __ i%2:
                rowSwap += 1
            __ board[0][i] __ i%2:
                colSwap += 1
        __ n//2 > rowSum or rowSum > (n+1)//2:
            r_ -1
        __ n//2 > colSum or colSum > (n+1)//2:
            r_ -1
        __ n % 2 __ 1:
            __ colSwap%2 __ 1:
                colSwap = n-colSwap
            __ rowSwap%2 __ 1:
                rowSwap = n-rowSwap
        ____
            colSwap = min(n-colSwap, colSwap)
            rowSwap = min(n-rowSwap, rowSwap)
        r_ (colSwap+rowSwap)//2
    
    ___ test(self
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
        ___ board in testCases:
            result = self.movesToChessboard(board)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
