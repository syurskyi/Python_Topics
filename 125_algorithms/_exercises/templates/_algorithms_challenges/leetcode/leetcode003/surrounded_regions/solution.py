class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    ___ solve(self, board
        n = le.(board)
        __ n __ 0:
            r_
        m = le.(board[0])
        __ m __ 0:
            r_
        self.n = n
        self.m = m
        # Go through the four edges to search O's
        ___ i in range(n
            ___ j in range(m
                __ i __ 0 or i __ n - 1 or j __ 0 or j __ m - 1:
                    __ board[i][j] __ 'O':
                        self.bfs(board, j, i)
        ___ i in range(n
            ___ j in range(m
                __ board[i][j] __ 'O':
                    board[i][j] = 'X'
                __ board[i][j] __ 'Y':
                    board[i][j] = 'O'

    ___ bfs(self, board, x, y
        """Use BFS to set O to Y"""
        queue = []
        board[y][x] = 'Y'
        queue.append((x, y))
        w___ queue:
            root_x, root_y = queue.pop(0)
            ___ node in self.adjacent(board, root_x, root_y
                x, y = node
                __ board[y][x] != 'Y':
                    board[y][x] = 'Y'
                    queue.append((x, y))

    ___ adjacent(self, board, x, y
        res = []
        __ x + 1 < self.m and board[y][x + 1] __ 'O':
            res.append((x + 1, y))
        __ x - 1 > 0 and board[y][x - 1] __ 'O':
            res.append((x - 1, y))
        __ y + 1 < self.n and board[y + 1][x] __ 'O':
            res.append((x, y + 1))
        __ y - 1 > 0 and board[y - 1][x] __ 'O':
            res.append((x, y - 1))
        r_ res
