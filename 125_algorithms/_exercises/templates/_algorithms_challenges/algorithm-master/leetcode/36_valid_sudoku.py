class Solution:
    ___ isValidSudoku(self, board
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        __ not board or not board[0] or le.(board) != le.(board[0]
            r_ False

        n = le.(board)
        EMPTY = '.'
        CANDS = '123456789'

        ___ x in range(n
            used = set()

            ___ y in range(n
                __ board[x][y] __ EMPTY:
                    continue
                __ board[x][y] not in CANDS:
                    r_ False
                __ board[x][y] in used:
                    r_ False
                used.add(board[x][y])

        ___ y in range(n
            used = set()

            ___ x in range(n
                __ board[x][y] __ EMPTY:
                    continue
                __ board[x][y] in used:
                    r_ False
                used.add(board[x][y])

        ___ i in range(3
            ___ j in range(3
                used = set()

                ___ x in range(i * 3, i * 3 + 3
                    ___ y in range(j * 3, j * 3 + 3
                        __ board[x][y] __ EMPTY:
                            continue
                        __ board[x][y] in used:
                            r_ False
                        used.add(board[x][y])

        r_ True
