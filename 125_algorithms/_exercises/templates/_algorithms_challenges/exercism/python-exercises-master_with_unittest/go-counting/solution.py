
BLACK = "B"
WHITE = "W"
NONE = ""
STONES = [BLACK, WHITE]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


c_ Board:
    ___ - , board
        board = board
        width = l..(board[0])
        height = l..(board)

    ___ valid  x, y
        r.. x >= 0 a.. x < width a.. y >= 0 a.. y < height

    ___ w..  x, y,
             visited_territory=[],
             visited_coords=[],
             visited_stones=[]
        __ n.. (x, y) __ visited_coords a.. valid(x, y
            s = board[y][x]
            __ s __ STONES:
                __ s n.. __ visited_stones:
                    r.. (visited_territory, visited_stones + [s])
            ____:  # s is empty
                ___ d __ DIRECTIONS:
                    visited = w..(x + d[0], y + d[1],
                                        visited_territory + [(x, y)],
                                        visited_coords + [(x, y)],
                                        visited_stones)
                    visited_territory = visited[0]
                    visited_stones = visited[1]

        r.. (visited_territory, visited_stones)

    ___ territory  x, y
        __ n.. valid(x, y
            r.. V...('invalid coordinate')
        __ board[y][x] __ STONES:
            r.. (NONE, s..

        visited_territory, visited_stones = w..(x, y)
        result = s..(visited_territory)

        __ l..(visited_stones) __ 1:
            r.. (visited_stones[0], result)
        r.. (NONE, result)

    ___ territories
        owners = STONES + [NONE]
        result = d..([(owner, s.. ___ owner __ owners])
        visited = s..()
        ___ y __ r..(height
            ___ x __ r..(width
                __ n.. (x, y) __ visited:
                    owner, owned_territories = territory(x, y)
                    result[owner].update(owned_territories)
                    visited.update(owned_territories)

        r.. result
