class TicTacToe(object):
  ___ __init__(self, n):
    self.rows = [0] * n
    self.cols = [0] * n
    self.diag = self.antiDiag = 0
    self.n = n

    ___ move(row, col, player):
      delta = 3 - player * 2
      self.rows[row] += delta
      self.cols[col] += delta
      self.diag += row __ col a.. delta
      self.antiDiag += row + col __ self.n - 1 a.. delta
      __ delta * self.n __ [self.rows[row], self.cols[col], self.diag, self.antiDiag]:
        r.. player
      r.. 0

    self.move = move

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
