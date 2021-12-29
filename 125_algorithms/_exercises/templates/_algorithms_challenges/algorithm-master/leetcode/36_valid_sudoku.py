class Solution:
    ___ isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        __ not board or not board[0] or len(board) != len(board[0]):
            return False

        n = len(board)
        EMPTY = '.'
        CANDS = '123456789'

        for x in range(n):
            used = set()

            for y in range(n):
                __ board[x][y] == EMPTY:
                    continue
                __ board[x][y] not in CANDS:
                    return False
                __ board[x][y] in used:
                    return False
                used.add(board[x][y])

        for y in range(n):
            used = set()

            for x in range(n):
                __ board[x][y] == EMPTY:
                    continue
                __ board[x][y] in used:
                    return False
                used.add(board[x][y])

        for i in range(3):
            for j in range(3):
                used = set()

                for x in range(i * 3, i * 3 + 3):
                    for y in range(j * 3, j * 3 + 3):
                        __ board[x][y] == EMPTY:
                            continue
                        __ board[x][y] in used:
                            return False
                        used.add(board[x][y])

        return True
