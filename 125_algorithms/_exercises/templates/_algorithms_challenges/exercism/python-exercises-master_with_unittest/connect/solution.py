
class ConnectGame:

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    white = "O"
    black = "X"
    none = ""

    ___ __init__(self, lines):
        self.board = self.make_board(lines)
        assert len(self.board) > 0

        self.width = len(self.board[0])
        self.height = len(self.board)
        assert self.width > 0 and self.height > 0

        for l in self.board:
            assert len(l) == self.width

    ___ valid(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    ___ make_board(self, lines):
        return ["".join(l.split()) for l in lines.splitlines()]

    ___ player_reach_dest(self, player, x, y):
        __ player == self.black:
            return x == self.width - 1
        __ player == self.white:
            return y == self.height - 1

    ___ walk_board(self, player, x, y, visited=[]):
        __ (x, y) in visited:
            return False

        __ (not self.valid(x, y)) or self.board[y][x] != player:
            return False

        __ self.player_reach_dest(player, x, y):
            return True

        for d in self.directions:
            __ self.walk_board(player, x + d[0], y + d[1], visited + [(x, y)]):
                return True

    ___ check_player_is_winner(self, player):
        __ player == self.black:
            for y in range(self.height):
                __ self.walk_board(player, 0, y):
                    return True
        __ player == self.white:
            for x in range(self.width):
                __ self.walk_board(player, x, 0):
                    return True

    ___ get_winner(self):
        __ self.check_player_is_winner(self.black):
            return self.black
        __ self.check_player_is_winner(self.white):
            return self.white
        return self.none
