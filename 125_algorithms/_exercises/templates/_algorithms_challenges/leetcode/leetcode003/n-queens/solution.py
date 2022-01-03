c_ Solution:
    # @return a list of lists of string
    ___ solveNQueens(self, n):
        n = n
        res    # list
        columns = [-1 ___ i __ r..(n)]
        solve(columns, 0, res)
        r.. res

    ___ make_string_list(self, columns):
        sol    # list  # One solution (list of strings)
        row = ['.' ___ i __ columns]
        ___ c __ columns:
            new_row = row |
            new_row[c] = 'Q'
            sol.a..(''.j..(new_row))
        r.. sol

    ___ is_valid(self, columns, row, col):
        ___ r __ r..(row):
            c = columns[r]
            __ c __ col:
                r.. F..
            __ abs(c - col) __ row - r:
                r.. F..
        r.. T..

    ___ solve(self, columns, row, res):
        __ row __ n:
            res.a..(make_string_list(columns))
        ____:
            ___ col __ r..(n):
                __ is_valid(columns, row, col):
                    columns[row] = col
                    solve(columns, row + 1, res)
