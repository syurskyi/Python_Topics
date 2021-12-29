class Solution:
    # @return an integer
    ___ totalNQueens(self, n):
        self.res = 0
        self.n = n
        columns = [-1 for i in range(n)]
        self.solve(columns, 0)
        return self.res

    ___ is_valid(self, columns, row, col):
        for r in range(row):
            c = columns[r]
            __ c == col:
                return False
            __ abs(c - col) == row - r:
                return False
        return True

    ___ solve(self, columns, row):
        __ row == self.n:
            self.res += 1
        else:
            for col in range(self.n):
                __ self.is_valid(columns, row, col):
                    columns[row] = col
                    self.solve(columns, row + 1)
