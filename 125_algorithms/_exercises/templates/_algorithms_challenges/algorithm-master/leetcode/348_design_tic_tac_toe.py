c_ TicTacToe(o..
    PLER_A = 1
    PLER_B = 2

    ___ - , n
        """
        Initialize your data structure here.
        :type n: int
        """
        R = [0] * n
        C = [0] * n
        DR = 0  # only one
        DL = 0  # only one

    ___ move  x, y, player
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
        n = l..(R)
        delta = 1 __ player __ PLER_A ____ -1
        R[x] += delta
        C[y] += delta
        DR += delta __ x __ y ____ 0  # x - y == 0
        DL += delta __ x __ n - 1 - y ____ 0  # x + y == n - 1
        r.. (a..(R[x]) __ n o.
                a..(C[y]) __ n o.
                a..(DR) __ n o.
                a..(DL) __ n)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(x,y,player)
