'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object):
    ___ movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        rowSum, colSum, rowSwap, colSwap = 0, 0, 0, 0
        for i in range(n):
            for j in range(n):
                __ board[0][0]^board[i][0]^board[0][j]^board[i][j] == 1:
                    return -1
        for i in range(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            __ board[i][0] == i%2:
                rowSwap += 1
            __ board[0][i] == i%2:
                colSwap += 1
        __ n//2 > rowSum or rowSum > (n+1)//2:
            return -1
        __ n//2 > colSum or colSum > (n+1)//2:
            return -1
        __ n % 2 == 1:
            __ colSwap%2 == 1:
                colSwap = n-colSwap
            __ rowSwap%2 == 1:
                rowSwap = n-rowSwap
        else:
            colSwap = min(n-colSwap, colSwap)
            rowSwap = min(n-rowSwap, rowSwap)
        return (colSwap+rowSwap)//2
    
    ___ test(self):
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
        for board in testCases:
            result = self.movesToChessboard(board)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
