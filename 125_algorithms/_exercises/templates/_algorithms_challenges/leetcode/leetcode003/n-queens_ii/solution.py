class Solution:
    # @return an integer
    ___ totalNQueens(self, n
        self.res = 0
        self.n = n
        columns = [-1 ___ i in range(n)]
        self.solve(columns, 0)
        r_ self.res

    ___ is_valid(self, columns, row, col
        ___ r in range(row
            c = columns[r]
            __ c __ col:
                r_ False
            __ abs(c - col) __ row - r:
                r_ False
        r_ True

    ___ solve(self, columns, row
        __ row __ self.n:
            self.res += 1
        ____
            ___ col in range(self.n
                __ self.is_valid(columns, row, col
                    columns[row] = col
                    self.solve(columns, row + 1)
