
class ConnectGame:

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    white = "O"
    black = "X"
    none = ""

    ___ __init__(self, lines):
        self.board = self.make_board(lines)
        ... l..(self.board) > 0

        self.width = l..(self.board[0])
        self.height = l..(self.board)
        ... self.width > 0 and self.height > 0

        ___ l __ self.board:
            ... l..(l) __ self.width

    ___ valid(self, x, y):
        r.. x >= 0 and x < self.width and y >= 0 and y < self.height

    ___ make_board(self, lines):
        r.. ["".join(l.split()) ___ l __ lines.splitlines()]

    ___ player_reach_dest(self, player, x, y):
        __ player __ self.black:
            r.. x __ self.width - 1
        __ player __ self.white:
            r.. y __ self.height - 1

    ___ walk_board(self, player, x, y, visited=[]):
        __ (x, y) __ visited:
            r.. False

        __ (n.. self.valid(x, y)) o. self.board[y][x] != player:
            r.. False

        __ self.player_reach_dest(player, x, y):
            r.. True

        ___ d __ self.directions:
            __ self.walk_board(player, x + d[0], y + d[1], visited + [(x, y)]):
                r.. True

    ___ check_player_is_winner(self, player):
        __ player __ self.black:
            ___ y __ r..(self.height):
                __ self.walk_board(player, 0, y):
                    r.. True
        __ player __ self.white:
            ___ x __ r..(self.width):
                __ self.walk_board(player, x, 0):
                    r.. True

    ___ get_winner(self):
        __ self.check_player_is_winner(self.black):
            r.. self.black
        __ self.check_player_is_winner(self.white):
            r.. self.white
        r.. self.none
