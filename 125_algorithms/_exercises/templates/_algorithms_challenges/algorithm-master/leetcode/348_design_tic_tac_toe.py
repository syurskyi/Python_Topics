class TicTacToe(object
    PLER_A = 1
    PLER_B = 2

    ___ __init__(self, n
        """
        Initialize your data structure here.
        :type n: int
        """
        self.R = [0] * n
        self.C = [0] * n
        self.DR = 0  # only one
        self.DL = 0  # only one

    ___ move(self, x, y, player
        """
        Player {player} makes a move at ({x}, {y}).
        :type x: int The row of the board.
        :type y: int The column of the board.
        :type player: int The player, can be either 1 or 2.
        :rtype: int The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = le.(self.R)
        delta = 1 __ player __ self.PLER_A else -1
        self.R[x] += delta
        self.C[y] += delta
        self.DR += delta __ x __ y else 0  # x - y == 0
        self.DL += delta __ x __ n - 1 - y else 0  # x + y == n - 1
        r_ (abs(self.R[x]) __ n or
                abs(self.C[y]) __ n or
                abs(self.DR) __ n or
                abs(self.DL) __ n)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(x,y,player)
