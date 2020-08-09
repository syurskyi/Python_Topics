class ConnectGame:
    ___ __init__(self, board
        self._board = [line.split() ___ line in board.splitlines()]
        self._players = {}
        self._players['X'] = (
            tuple((0, r) ___ r in range(le.(self._board))),
            tuple((le.(row)-1, r) ___ r, row in enumerate(self._board)))
        self._players['O'] = (
            tuple((c, 0) ___ c in range(le.(self._board[0]))),
            tuple((c, le.(self._board)-1) ___ c in range(le.(self._board[-1]))))

    ___ get_winner(self
        ___ player in self._players.keys(
            __ self._find_path(player
                r_ player
        r_ ''

    ___ _find_path(self, player
        start, end = self._players[player]
        """Dijkstras path finding algorithm"""
        queue = list(start)
        seen = set()
        w___ queue:
            x, y = queue.pop()
            __ (x, y) in seen:
                continue
            seen.add((x, y))
            __ not (0 <= y < le.(self._board) and 0 <= x < le.(self._board[y])) or \
                    self._board[y][x] != player:
                continue
            __ (x, y) in end:
                r_ True
            queue.extend((x+r,y+s) ___ r, s in
                    ((0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1)))
        r_ False
