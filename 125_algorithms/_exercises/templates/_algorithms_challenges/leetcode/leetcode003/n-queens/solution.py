class Solution:
    # @return a list of lists of string
    ___ solveNQueens(self, n
        self.n = n
        res = []
        columns = [-1 for i in range(n)]
        self.solve(columns, 0, res)
        r_ res

    ___ make_string_list(self, columns
        sol = []  # One solution (list of strings)
        row = ['.' for i in columns]
        for c in columns:
            new_row = row[:]
            new_row[c] = 'Q'
            sol.append(''.join(new_row))
        r_ sol

    ___ is_valid(self, columns, row, col
        for r in range(row
            c = columns[r]
            __ c __ col:
                r_ False
            __ abs(c - col) __ row - r:
                r_ False
        r_ True

    ___ solve(self, columns, row, res
        __ row __ self.n:
            res.append(self.make_string_list(columns))
        ____
            for col in range(self.n
                __ self.is_valid(columns, row, col
                    columns[row] = col
                    self.solve(columns, row + 1, res)
