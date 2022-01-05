c_ Solution:
    ___ solveSudoku  board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ n.. board o. n.. board[0] o. l..(board) != l..(board[0]):
            r..

        dfs(board, 0, 0)

    ___ dfs  board, x, y):
        n = l..(board)

        __ x __ n:
            r.. T..

        _x, _y = x, y + 1

        __ y __ n - 1:
            _x = x + 1
            _y = 0

        __ board[x][y] != '.':
            __ n.. is_valid(board, x, y):
                r.. F..
            r.. dfs(board, _x, _y)

        ___ i __ r..(1, n + 1):
            board[x][y] = s..(i)
            __ (
                is_valid(board, x, y) a..
                dfs(board, _x, _y)
            ):
                r.. T..

        board[x][y] = '.'
        r.. F..

    ___ is_valid  board, x, y):
        __ board[x][y] n.. __ '123456789':
            r.. F..

        n = l..(board)

        ___ i __ r..(n):
            __ y != i a.. board[x][y] __ board[x][i]:
                r.. F..
            __ x != i a.. board[x][y] __ board[i][y]:
                r.. F..

        r = x // 3 * 3
        c = y // 3 * 3

        ___ i __ r..(r, r + 3):
            ___ j __ r..(c, c + 3):
                __ x __ i a.. y __ j:
                    _____
                __ board[x][y] __ board[i][j]:
                    r.. F..

        r.. T..
