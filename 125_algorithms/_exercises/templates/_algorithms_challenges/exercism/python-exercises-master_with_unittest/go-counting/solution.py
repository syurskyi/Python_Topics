
BLACK = "B"
WHITE = "W"
NONE = ""
STONES = [BLACK, WHITE]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Board:
    ___ __init__(self, board):
        self.board = board
        self.width = l..(self.board[0])
        self.height = l..(self.board)

    ___ valid(self, x, y):
        r.. x >= 0 a.. x < self.width a.. y >= 0 a.. y < self.height

    ___ walk(self, x, y,
             visited_territory=[],
             visited_coords=[],
             visited_stones=[]):
        __ n.. (x, y) __ visited_coords a.. self.valid(x, y):
            s = self.board[y][x]
            __ s __ STONES:
                __ s n.. __ visited_stones:
                    r.. (visited_territory, visited_stones + [s])
            ____:  # s is empty
                ___ d __ DIRECTIONS:
                    visited = self.walk(x + d[0], y + d[1],
                                        visited_territory + [(x, y)],
                                        visited_coords + [(x, y)],
                                        visited_stones)
                    visited_territory = visited[0]
                    visited_stones = visited[1]

        r.. (visited_territory, visited_stones)

    ___ territory(self, x, y):
        __ n.. self.valid(x, y):
            raise ValueError('invalid coordinate')
        __ self.board[y][x] __ STONES:
            r.. (NONE, set())

        visited_territory, visited_stones = self.walk(x, y)
        result = set(visited_territory)

        __ l..(visited_stones) __ 1:
            r.. (visited_stones[0], result)
        r.. (NONE, result)

    ___ territories(self):
        owners = STONES + [NONE]
        result = d..([(owner, set()) ___ owner __ owners])
        visited = set()
        ___ y __ r..(self.height):
            ___ x __ r..(self.width):
                __ n.. (x, y) __ visited:
                    owner, owned_territories = self.territory(x, y)
                    result[owner].update(owned_territories)
                    visited.update(owned_territories)

        r.. result
