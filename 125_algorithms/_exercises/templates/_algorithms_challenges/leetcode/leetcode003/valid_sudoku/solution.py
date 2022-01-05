"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules
(http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.

A valid Sudoku board (partially filled) is not necessarily solvable. Only the
filled cells need to be validated.

"""

c_ Solution(object):
    ___ isValidSudoku  board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        ___ i __ r..(9):
            d    # dict
            ___ j __ r..(9):
                __ board[i][j] __ '.':
                    p..
                ____ board[i][j] __ d:
                    r.. F..
                ____:
                    d[board[i][j]] = T..
        # Check columns
        ___ j __ r..(9):
            d    # dict
            ___ i __ r..(9):
                __ board[i][j] __ '.':
                    p..
                ____ board[i][j] __ d:
                    r.. F..
                ____:
                    d[board[i][j]] = T..
        # Check sub-boxes
        ___ m __ r..(0, 9, 3):
            ___ n __ r..(0, 9, 3):
                d    # dict
                ___ i __ r..(n, n + 3):
                    ___ j __ r..(m, m + 3):
                        __ board[i][j] __ '.':
                            p..
                        ____ board[i][j] __ d:
                            r.. F..
                        ____:
                            d[board[i][j]] = T..
        r.. T..
