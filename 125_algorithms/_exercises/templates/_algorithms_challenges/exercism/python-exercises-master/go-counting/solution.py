
BLACK = "B"
WHITE = "W"
NONE = ""
STONES = [BLACK, WHITE]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Board:
    ___ __init__(self, board
        self.board = board
        self.width = le.(self.board[0])
        self.height = le.(self.board)

    ___ valid(self, x, y
        r_ x >= 0 and x < self.width and y >= 0 and y < self.height

    ___ walk(self, x, y,
             visited_territory=  # list,
             visited_coords=  # list,
             visited_stones=  # list
        __ not (x, y) __ visited_coords and self.valid(x, y
            s = self.board[y][x]
            __ s __ STONES:
                __ s not __ visited_stones:
                    r_ (visited_territory, visited_stones + [s])
            ____  # s is empty
                ___ d __ DIRECTIONS:
                    visited = self.walk(x + d[0], y + d[1],
                                        visited_territory + [(x, y)],
                                        visited_coords + [(x, y)],
                                        visited_stones)
                    visited_territory = visited[0]
                    visited_stones = visited[1]

        r_ (visited_territory, visited_stones)

    ___ territory(self, x, y
        __ not self.valid(x, y
            raise ValueError('invalid coordinate')
        __ self.board[y][x] __ STONES:
            r_ (NONE, set())

        visited_territory, visited_stones = self.walk(x, y)
        result = set(visited_territory)

        __ le.(visited_stones) __ 1:
            r_ (visited_stones[0], result)
        r_ (NONE, result)

    ___ territories(self
        owners = STONES + [NONE]
        result = dict([(owner, set()) ___ owner __ owners])
        visited = set()
        ___ y __ range(self.height
            ___ x __ range(self.width
                __ not (x, y) __ visited:
                    owner, owned_territories = self.territory(x, y)
                    result[owner].update(owned_territories)
                    visited.update(owned_territories)

        r_ result
