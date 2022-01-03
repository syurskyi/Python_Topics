"""
Conway's Game of Life - Unlimited Edition
http://www.codewars.com/kata/52423db9add6f6fc39000354/train/python
"""

____ copy _______ deepcopy


___ get_generation(cells, generations):
    origin = deepcopy(cells)
    __ generations __ 0:
        r.. origin
    __ generations > 1:
        origin = get_generation(origin, generations - 1)

    ___ row __ origin:
        row.insert(0, 0)
        row.a..(0)
    origin.insert(0, [0] * l..(origin[0]))
    origin.a..([0] * l..(origin[0]))

    result = deepcopy(origin)
    ___ r __ r..(l..(origin)):
        ___ c __ r..(l..(origin[0])):
            neighbours = get_living_neighbours(origin, r, c)
            __ neighbours > 3 o. neighbours < 2:
                result[r][c] = 0
            ____ neighbours __ 3:
                result[r][c] = 1

    trim_result(result)

    r.. result


___ trim_result(result):
    w.... is_row_all_empty(result[0]):
        result.pop(0)
    w.... is_row_all_empty(result[-1]):
        result.pop()
    start_empty, end_empty = T.., T..
    w.... start_empty o. end_empty:
        ___ r __ result:
            __ r[0] != 0:
                start_empty = F..
            __ r[-1] != 0:
                end_empty = F..
        ___ r __ result:
            __ start_empty:
                r.pop(0)
            __ end_empty:
                r.pop()


___ is_row_all_empty(row):
    r.. s..(row) __ 0


___ get_living_neighbours(cells, row, col):
    livings = 0
    ___ r __ [-1, 0, 1]:
        __ 0 <= row + r <= l..(cells) - 1:
            ___ c __ [-1, 0, 1]:
                __ 0 <= col + c <= l..(cells[0]) - 1:
                    __ c __ 0 a.. r __ 0:
                        continue
                    livings += cells[row + r][col + c]
    r.. livings