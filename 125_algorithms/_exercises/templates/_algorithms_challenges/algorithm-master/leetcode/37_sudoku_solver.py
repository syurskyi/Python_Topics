class Solution:
    ___ solveSudoku(self, board
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ not board or not board[0] or le.(board) != le.(board[0]
            r_

        self.dfs(board, 0, 0)

    ___ dfs(self, board, x, y
        n = le.(board)

        __ x __ n:
            r_ True

        _x, _y = x, y + 1

        __ y __ n - 1:
            _x = x + 1
            _y = 0

        __ board[x][y] != '.':
            __ not self.is_valid(board, x, y
                r_ False
            r_ self.dfs(board, _x, _y)

        for i in range(1, n + 1
            board[x][y] = str(i)
            __ (
                self.is_valid(board, x, y) and
                self.dfs(board, _x, _y)

                r_ True

        board[x][y] = '.'
        r_ False

    ___ is_valid(self, board, x, y
        __ board[x][y] not in '123456789':
            r_ False

        n = le.(board)

        for i in range(n
            __ y != i and board[x][y] __ board[x][i]:
                r_ False
            __ x != i and board[x][y] __ board[i][y]:
                r_ False

        r = x // 3 * 3
        c = y // 3 * 3

        for i in range(r, r + 3
            for j in range(c, c + 3
                __ x __ i and y __ j:
                    continue
                __ board[x][y] __ board[i][j]:
                    r_ False

        r_ True
