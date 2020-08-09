______ copy


class Point(object
    ___ __init__(self, x, y
        self.x = x
        self.y = y

    ___ __repr__(self
        r_ 'Point({}:{})'.format(self.x, self.y)

    ___ __add__(self, other
        r_ Point(self.x + other.x, self.y + other.y)

    ___ __sub__(self, other
        r_ Point(self.x - other.x, self.y - other.y)

    ___ __eq__(self, other
        r_ self.x __ other.x and self.y __ other.y

    ___ __ne__(self, other
        r_ not (self __ other)


DIRECTIONS = (Point(1, 0), Point(1, -1), Point(1, 1), Point(-1, -1),
              Point(0, -1), Point(0, 1), Point(-1, 1), Point(-1, 0))


class WordSearch(object
    ___ __init__(self, puzzle
        self.rows = puzzle.split()
        self.width = le.(self.rows[0])
        self.height = le.(self.rows)

    ___ find_char(self, coordinate
        __ coordinate.x < 0 or coordinate.x >= self.width:
            r_
        __ coordinate.y < 0 or coordinate.y >= self.height:
            r_
        r_ self.rows[coordinate.y][coordinate.x]

    ___ find(self, word, position, direction
        current = copy.copy(position)
        ___ letter in word:
            __ self.find_char(current) != letter:
                r_
            current += direction
        r_ position, current - direction

    ___ search(self, word
        positions = (Point(x, y)
                     ___ x in range(self.width) ___ y in range(self.height))
        ___ pos in positions:
            ___ d in DIRECTIONS:
                result = self.find(word, pos, d)
                __ result:
                    r_ result
        r_ None
