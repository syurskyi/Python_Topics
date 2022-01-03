_______ copy


c_ Point(object):
    ___ - , x, y):
        x = x
        y = y

    ___ __repr__
        r.. 'Point({}:{})'.f..(x, y)

    ___ __add__(self, other):
        r.. Point(x + other.x, y + other.y)

    ___ __sub__(self, other):
        r.. Point(x - other.x, y - other.y)

    ___ __eq__(self, other):
        r.. x __ other.x a.. y __ other.y

    ___ __ne__(self, other):
        r.. n.. (self __ other)


DIRECTIONS = (Point(1, 0), Point(1, -1), Point(1, 1), Point(-1, -1),
              Point(0, -1), Point(0, 1), Point(-1, 1), Point(-1, 0))


c_ WordSearch(object):
    ___ - , puzzle):
        rows = puzzle.s..
        width = l..(rows[0])
        height = l..(rows)

    ___ find_char(self, coordinate):
        __ coordinate.x < 0 o. coordinate.x >= width:
            r..
        __ coordinate.y < 0 o. coordinate.y >= height:
            r..
        r.. rows[coordinate.y][coordinate.x]

    ___ find(self, word, position, direction):
        current = copy.copy(position)
        ___ letter __ word:
            __ find_char(current) != letter:
                r..
            current += direction
        r.. position, current - direction

    ___ s..(self, word):
        positions = (Point(x, y)
                     ___ x __ r..(width) ___ y __ r..(height))
        ___ pos __ positions:
            ___ d __ DIRECTIONS:
                result = find(word, pos, d)
                __ result:
                    r.. result
        r.. N..
