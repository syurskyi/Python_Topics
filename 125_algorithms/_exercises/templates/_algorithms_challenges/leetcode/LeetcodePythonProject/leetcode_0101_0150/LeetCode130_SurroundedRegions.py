'''
Created on Feb 8, 2017

@author: MT
'''
class Solution(object
    ___ solve(self, board
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ not board or le.(board) <= 1 or le.(board[0]) <= 1: r_
        m, n = le.(board), le.(board[0])
        for i in range(m
            __ board[i][0] __ 'O':
                self.bfs(board, i, 0)
            __ board[i][n-1] __ 'O':
                self.bfs(board, i, n-1)
        for i in range(n
            __ board[0][i] __ 'O':
                self.bfs(board, 0, i)
            __ board[m-1][i] __ 'O':
                self.bfs(board, m-1, i)
        for i in range(m
            for j in range(n
                __ board[i][j] __ 'O':
                    board[i][j] = 'X'
                __ board[i][j] __ '#':
                    board[i][j] = 'O'
    
    ___ bfs(self, board, x, y
        board[x][y] = '#'
        m, n = le.(board), le.(board[0])
        index = x*n+y
        queue = [index]
        w___ queue:
            nextInd = queue.pop(0)
            i = int(nextInd/n)
            j = nextInd%n
            __ i > 1 and board[i-1][j] __ 'O':
                board[i-1][j] = '#'
                queue.append((i-1)*n+j)
            __ j > 1 and board[i][j-1] __ 'O':
                board[i][j-1] = '#'
                queue.append(i*n+j-1)
            __ i+1 < m and board[i+1][j] __ 'O':
                board[i+1][j] = '#'
                queue.append((i+1)*n+j)
            __ j+1 < n and board[i][j+1] __ 'O':
                board[i][j+1] = '#'
                queue.append(i*n+j+1)
    
    ___ test(self
        testCases = [
            [
                'XXXX',
                'XOOX',
                'XXOX',
                'XOXX',
            ],
        ]
        for matrix in testCases:
            board = [list(l) for l in matrix]
            print('before')
            print('%s' % (board))
            self.solve(board)
            print('after')
            print('%s' % (board))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()