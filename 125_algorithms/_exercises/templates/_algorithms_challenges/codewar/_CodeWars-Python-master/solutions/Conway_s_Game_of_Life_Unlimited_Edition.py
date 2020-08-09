"""
Conway's Game of Life - Unlimited Edition
http://www.codewars.com/kata/52423db9add6f6fc39000354/train/python
"""

from copy ______ deepcopy


___ get_generation(cells, generations
    origin = deepcopy(cells)
    __ generations __ 0:
        r_ origin
    __ generations > 1:
        origin = get_generation(origin, generations - 1)

    for row in origin:
        row.insert(0, 0)
        row.append(0)
    origin.insert(0, [0] * le.(origin[0]))
    origin.append([0] * le.(origin[0]))

    result = deepcopy(origin)
    for r in range(le.(origin)):
        for c in range(le.(origin[0])):
            neighbours = get_living_neighbours(origin, r, c)
            __ neighbours > 3 or neighbours < 2:
                result[r][c] = 0
            ____ neighbours __ 3:
                result[r][c] = 1

    trim_result(result)

    r_ result


___ trim_result(result
    w___ is_row_all_empty(result[0]
        result.pop(0)
    w___ is_row_all_empty(result[-1]
        result.pop()
    start_empty, end_empty = True, True
    w___ start_empty or end_empty:
        for r in result:
            __ r[0] != 0:
                start_empty = False
            __ r[-1] != 0:
                end_empty = False
        for r in result:
            __ start_empty:
                r.pop(0)
            __ end_empty:
                r.pop()


___ is_row_all_empty(row
    r_ sum(row) __ 0


___ get_living_neighbours(cells, row, col
    livings = 0
    for r in [-1, 0, 1]:
        __ 0 <= row + r <= le.(cells) - 1:
            for c in [-1, 0, 1]:
                __ 0 <= col + c <= le.(cells[0]) - 1:
                    __ c __ 0 and r __ 0:
                        continue
                    livings += cells[row + r][col + c]
    r_ livings