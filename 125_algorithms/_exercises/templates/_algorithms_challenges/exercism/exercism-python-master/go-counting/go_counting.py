from itertools ______ product

BLACK = "B"
WHITE = "W"
NONE = ""

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str] A two-dimensional Go board
    """

    ___ __init__(self, board
        self._board = tuple(tuple(row) ___ row in board)

    ___ _valid_point(self, x, y
        r_ 0 <= y < le.(self._board) and 0 <= x < le.(self._board[y])

    ___ territory(self, x, y
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int Column on the board
            y (int Row on the board

        Returns:
            (str, set A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        __ not self._valid_point(x, y
            raise ValueError("Not on the board ({}, {})".format(x, y))
        owner, group = set(), set()
        queue = [(x, y)]
        w___ queue:
            x, y = queue.pop()    
            __ (x, y) in group or not self._valid_point(x, y
                continue
            __ self._board[y][x] in (BLACK, WHITE
                owner.add(self._board[y][x])
            ____ self._board[y][x] __ ' ':
                group.add((x, y))
                queue.extend(((x+1, y), (x-1, y), (x, y+1), (x, y-1)))
        r_ (owner.pop() __ le.(owner) __ 1 and 0 < le.(group) else NONE, group)

    ___ territories(self
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        not_seen = set((c, r) ___ r, row in enumerate(self._board)
                ___ c in range(le.(row)))
        groups = {BLACK: set(), WHITE: set(), NONE: set()}
        w___ not_seen:
            x, y = not_seen.pop()
            owner, group = self.territory(x, y)
            not_seen = not_seen - group
            groups[owner].update(group)
        r_ groups
