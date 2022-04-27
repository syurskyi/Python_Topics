_______ p__

____ island _______ island_size

rectangle [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0]]

small [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]

empty [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

whole [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]


?p__.m__.p. "map_, expected", [
    (rectangle, 12),
    (small, 4),
    (empty, 0),
    (whole, 16),
])
___ test_island_size(map_, e..
    ... island_size(map_) __ e..