"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules
(http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.

A valid Sudoku board (partially filled) is not necessarily solvable. Only the
filled cells need to be validated.

"""

class Solution(object
    ___ isValidSudoku(self, board
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        for i in range(9
            d = {}
            for j in range(9
                __ board[i][j] __ '.':
                    pass
                ____ board[i][j] in d:
                    r_ False
                ____
                    d[board[i][j]] = True
        # Check columns
        for j in range(9
            d = {}
            for i in range(9
                __ board[i][j] __ '.':
                    pass
                ____ board[i][j] in d:
                    r_ False
                ____
                    d[board[i][j]] = True
        # Check sub-boxes
        for m in range(0, 9, 3
            for n in range(0, 9, 3
                d = {}
                for i in range(n, n + 3
                    for j in range(m, m + 3
                        __ board[i][j] __ '.':
                            pass
                        ____ board[i][j] in d:
                            r_ False
                        ____
                            d[board[i][j]] = True
        r_ True
