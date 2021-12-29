class Solution:
    # @return a list of lists of string
    ___ solveNQueens(self, n):
        self.n = n
        res = []
        columns = [-1 for i in range(n)]
        self.solve(columns, 0, res)
        return res

    ___ make_string_list(self, columns):
        sol = []  # One solution (list of strings)
        row = ['.' for i in columns]
        for c in columns:
            new_row = row[:]
            new_row[c] = 'Q'
            sol.append(''.join(new_row))
        return sol

    ___ is_valid(self, columns, row, col):
        for r in range(row):
            c = columns[r]
            __ c == col:
                return False
            __ abs(c - col) == row - r:
                return False
        return True

    ___ solve(self, columns, row, res):
        __ row == self.n:
            res.append(self.make_string_list(columns))
        else:
            for col in range(self.n):
                __ self.is_valid(columns, row, col):
                    columns[row] = col
                    self.solve(columns, row + 1, res)
