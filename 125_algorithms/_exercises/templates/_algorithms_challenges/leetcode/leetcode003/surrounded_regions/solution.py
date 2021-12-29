class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    ___ solve(self, board):
        n = l..(board)
        __ n __ 0:
            r..
        m = l..(board[0])
        __ m __ 0:
            r..
        self.n = n
        self.m = m
        # Go through the four edges to search O's
        ___ i __ r..(n):
            ___ j __ r..(m):
                __ i __ 0 o. i __ n - 1 o. j __ 0 o. j __ m - 1:
                    __ board[i][j] __ 'O':
                        self.bfs(board, j, i)
        ___ i __ r..(n):
            ___ j __ r..(m):
                __ board[i][j] __ 'O':
                    board[i][j] = 'X'
                __ board[i][j] __ 'Y':
                    board[i][j] = 'O'

    ___ bfs(self, board, x, y):
        """Use BFS to set O to Y"""
        queue    # list
        board[y][x] = 'Y'
        queue.a..((x, y))
        while queue:
            root_x, root_y = queue.pop(0)
            ___ node __ self.adjacent(board, root_x, root_y):
                x, y = node
                __ board[y][x] != 'Y':
                    board[y][x] = 'Y'
                    queue.a..((x, y))

    ___ adjacent(self, board, x, y):
        res    # list
        __ x + 1 < self.m and board[y][x + 1] __ 'O':
            res.a..((x + 1, y))
        __ x - 1 > 0 and board[y][x - 1] __ 'O':
            res.a..((x - 1, y))
        __ y + 1 < self.n and board[y + 1][x] __ 'O':
            res.a..((x, y + 1))
        __ y - 1 > 0 and board[y - 1][x] __ 'O':
            res.a..((x, y - 1))
        r.. res
