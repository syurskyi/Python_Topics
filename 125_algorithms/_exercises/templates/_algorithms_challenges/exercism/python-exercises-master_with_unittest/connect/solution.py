
c_ ConnectGame:

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    white = "O"
    black = "X"
    none = ""

    ___ - , lines):
        board = make_board(lines)
        ... l..(board) > 0

        width = l..(board[0])
        height = l..(board)
        ... width > 0 a.. height > 0

        ___ l __ board:
            ... l..(l) __ width

    ___ valid(self, x, y):
        r.. x >= 0 a.. x < width a.. y >= 0 a.. y < height

    ___ make_board(self, lines):
        r.. ["".j..(l.s..()) ___ l __ lines.splitlines()]

    ___ player_reach_dest(self, player, x, y):
        __ player __ black:
            r.. x __ width - 1
        __ player __ white:
            r.. y __ height - 1

    ___ walk_board(self, player, x, y, visited=[]):
        __ (x, y) __ visited:
            r.. F..

        __ (n.. valid(x, y)) o. board[y][x] != player:
            r.. F..

        __ player_reach_dest(player, x, y):
            r.. T..

        ___ d __ directions:
            __ walk_board(player, x + d[0], y + d[1], visited + [(x, y)]):
                r.. T..

    ___ check_player_is_winner(self, player):
        __ player __ black:
            ___ y __ r..(height):
                __ walk_board(player, 0, y):
                    r.. T..
        __ player __ white:
            ___ x __ r..(width):
                __ walk_board(player, x, 0):
                    r.. T..

    ___ get_winner
        __ check_player_is_winner(black):
            r.. black
        __ check_player_is_winner(white):
            r.. white
        r.. none
