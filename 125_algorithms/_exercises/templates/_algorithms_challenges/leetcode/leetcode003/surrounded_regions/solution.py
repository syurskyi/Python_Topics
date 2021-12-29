class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    ___ solve(self, board):
        n = len(board)
        __ n == 0:
            return
        m = len(board[0])
        __ m == 0:
            return
        self.n = n
        self.m = m
        # Go through the four edges to search O's
        for i in range(n):
            for j in range(m):
                __ i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    __ board[i][j] == 'O':
                        self.bfs(board, j, i)
        for i in range(n):
            for j in range(m):
                __ board[i][j] == 'O':
                    board[i][j] = 'X'
                __ board[i][j] == 'Y':
                    board[i][j] = 'O'

    ___ bfs(self, board, x, y):
        """Use BFS to set O to Y"""
        queue = []
        board[y][x] = 'Y'
        queue.append((x, y))
        while queue:
            root_x, root_y = queue.pop(0)
            for node in self.adjacent(board, root_x, root_y):
                x, y = node
                __ board[y][x] != 'Y':
                    board[y][x] = 'Y'
                    queue.append((x, y))

    ___ adjacent(self, board, x, y):
        res = []
        __ x + 1 < self.m and board[y][x + 1] == 'O':
            res.append((x + 1, y))
        __ x - 1 > 0 and board[y][x - 1] == 'O':
            res.append((x - 1, y))
        __ y + 1 < self.n and board[y + 1][x] == 'O':
            res.append((x, y + 1))
        __ y - 1 > 0 and board[y - 1][x] == 'O':
            res.append((x, y - 1))
        return res
