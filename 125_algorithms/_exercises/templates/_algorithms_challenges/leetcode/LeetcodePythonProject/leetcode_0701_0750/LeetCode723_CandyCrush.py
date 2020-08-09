'''
Created on Feb 20, 2018

@author: tongq
'''
class Solution(object
    ___ candyCrush(self, board
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = le.(board), le.(board[0])
        res = [[0]*n ___ _ in range(m)]
        w___ True:
            changed = False
            ___ i in range(m
                ___ j in range(n
                    changed = self.bfs(board, i, j) or changed
            __ not changed:
                res = board
                break
            self.convert(res, board)
            board = res
        r_ res
    
    ___ bfs(self, board, i, j
        __ board[i][j] __ 0: r_ False
        m, n = le.(board), le.(board[0])
        val = abs(board[i][j])
        changed = False
        __ i+2 < m and val __ abs(board[i+1][j]) __ abs(board[i+2][j]
            ___ i0 in range(i+1, m
                __ abs(board[i0][j]) __ val:
                    board[i0][j] = -val
                ____
                    break
            changed = True
        __ j+2 < n and val __ abs(board[i][j+1]) __ abs(board[i][j+2]
            ___ j0 in range(j+1, n
                __ abs(board[i][j0]) __ val:
                    board[i][j0] = -val
                ____
                    break
            changed = True
        __ changed:
            board[i][j] = -val
        r_ changed
    
    ___ convert(self, res, board
        m, n = le.(res), le.(res[0])
        ___ j in range(n
            i0 = m-1
            ___ i in range(m-1, -1, -1
                __ board[i][j] > 0:
                    res[i0][j] = board[i][j]
                    i0 -= 1
            ___ i in range(i0, -1, -1
                res[i][j] = 0
    
    ___ test(self
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
        ___ board in testCases:
            print('board:')
            print('\n'.join([str(row) ___ row in board]))
            result = self.candyCrush(board)
            print('result:')
            print('\n'.join([str(row) ___ row in result]))
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
