
class ConnectGame:

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    white = "O"
    black = "X"
    none = ""

    ___ __init__(self, lines
        self.board = self.make_board(lines)
        assert le.(self.board) > 0

        self.width = le.(self.board[0])
        self.height = le.(self.board)
        assert self.width > 0 and self.height > 0

        for l in self.board:
            assert le.(l) __ self.width

    ___ valid(self, x, y
        r_ x >= 0 and x < self.width and y >= 0 and y < self.height

    ___ make_board(self, lines
        r_ ["".join(l.split()) for l in lines.splitlines()]

    ___ player_reach_dest(self, player, x, y
        __ player __ self.black:
            r_ x __ self.width - 1
        __ player __ self.white:
            r_ y __ self.height - 1

    ___ walk_board(self, player, x, y, visited=[]
        __ (x, y) in visited:
            r_ False

        __ (not self.valid(x, y)) or self.board[y][x] != player:
            r_ False

        __ self.player_reach_dest(player, x, y
            r_ True

        for d in self.directions:
            __ self.walk_board(player, x + d[0], y + d[1], visited + [(x, y)]
                r_ True

    ___ check_player_is_winner(self, player
        __ player __ self.black:
            for y in range(self.height
                __ self.walk_board(player, 0, y
                    r_ True
        __ player __ self.white:
            for x in range(self.width
                __ self.walk_board(player, x, 0
                    r_ True

    ___ get_winner(self
        __ self.check_player_is_winner(self.black
            r_ self.black
        __ self.check_player_is_winner(self.white
            r_ self.white
        r_ self.none
