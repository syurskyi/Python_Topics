class Solution:
    # @return an integer
    ___ totalNQueens(self, n):
        self.res = 0
        self.n = n
        columns = [-1 ___ i __ r..(n)]
        self.solve(columns, 0)
        r.. self.res

    ___ is_valid(self, columns, row, col):
        ___ r __ r..(row):
            c = columns[r]
            __ c __ col:
                r.. False
            __ abs(c - col) __ row - r:
                r.. False
        r.. True

    ___ solve(self, columns, row):
        __ row __ self.n:
            self.res += 1
        ____:
            ___ col __ r..(self.n):
                __ self.is_valid(columns, row, col):
                    columns[row] = col
                    self.solve(columns, row + 1)
