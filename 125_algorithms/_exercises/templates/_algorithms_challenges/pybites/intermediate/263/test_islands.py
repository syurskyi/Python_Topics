_______ p__

____ islands _______ count_islands

squares [[1, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 0]]

sparse [[1, 0, 1],
          [0, 1, 0],
          [1, 0, 1]]

empty [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

bad_map [[]]

circles [[1, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 0],
           [1, 0, 0, 1, 1, 0],
           [1, 1, 1, 1, 0, 0]]


?p__.m__.p.("data, expected", [
    (squares, 2),
    (sparse, 5),
    (empty, 0),
    (bad_map, 0),
    (circles, 1),
])
___ test_count_islands(data, e..
    ... count_islands(data) __ e..