c_ Solution:
    ___ isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        __ n.. board o. n.. board[0] o. l..(board) != l..(board[0]):
            r.. F..

        n = l..(board)
        EMPTY = '.'
        CANDS = '123456789'

        ___ x __ r..(n):
            used = set()

            ___ y __ r..(n):
                __ board[x][y] __ EMPTY:
                    continue
                __ board[x][y] n.. __ CANDS:
                    r.. F..
                __ board[x][y] __ used:
                    r.. F..
                used.add(board[x][y])

        ___ y __ r..(n):
            used = set()

            ___ x __ r..(n):
                __ board[x][y] __ EMPTY:
                    continue
                __ board[x][y] __ used:
                    r.. F..
                used.add(board[x][y])

        ___ i __ r..(3):
            ___ j __ r..(3):
                used = set()

                ___ x __ r..(i * 3, i * 3 + 3):
                    ___ y __ r..(j * 3, j * 3 + 3):
                        __ board[x][y] __ EMPTY:
                            continue
                        __ board[x][y] __ used:
                            r.. F..
                        used.add(board[x][y])

        r.. T..
