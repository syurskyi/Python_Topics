class Solution:
    ___ solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ n.. board o. n.. board[0] o. l..(board) != l..(board[0]):
            r..

        self.dfs(board, 0, 0)

    ___ dfs(self, board, x, y):
        n = l..(board)

        __ x __ n:
            r.. True

        _x, _y = x, y + 1

        __ y __ n - 1:
            _x = x + 1
            _y = 0

        __ board[x][y] != '.':
            __ n.. self.is_valid(board, x, y):
                r.. False
            r.. self.dfs(board, _x, _y)

        ___ i __ r..(1, n + 1):
            board[x][y] = str(i)
            __ (
                self.is_valid(board, x, y) and
                self.dfs(board, _x, _y)
            ):
                r.. True

        board[x][y] = '.'
        r.. False

    ___ is_valid(self, board, x, y):
        __ board[x][y] n.. __ '123456789':
            r.. False

        n = l..(board)

        ___ i __ r..(n):
            __ y != i and board[x][y] __ board[x][i]:
                r.. False
            __ x != i and board[x][y] __ board[i][y]:
                r.. False

        r = x // 3 * 3
        c = y // 3 * 3

        ___ i __ r..(r, r + 3):
            ___ j __ r..(c, c + 3):
                __ x __ i and y __ j:
                    continue
                __ board[x][y] __ board[i][j]:
                    r.. False

        r.. True
