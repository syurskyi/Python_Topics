c_ TicTacToe(o..
  ___ - , n
    rows [0] * n
    cols [0] * n
    diag antiDiag 0
    n n

    ___ move(row, col, player
      delta 3 - player * 2
      rows[row] += delta
      cols[col] += delta
      diag += row __ col a.. delta
      antiDiag += row + col __ n - 1 a.. delta
      __ delta * n __ [rows[row], cols[col], diag, antiDiag]:
        r.. player
      r.. 0

    move move

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
