import copy


class Point(object):
    ___ __init__(self, x, y):
        self.x = x
        self.y = y

    ___ __repr__(self):
        return 'Point({}:{})'.format(self.x, self.y)

    ___ __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    ___ __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    ___ __eq__(self, other):
        return self.x == other.x and self.y == other.y

    ___ __ne__(self, other):
        return not (self == other)


DIRECTIONS = (Point(1, 0), Point(1, -1), Point(1, 1), Point(-1, -1),
              Point(0, -1), Point(0, 1), Point(-1, 1), Point(-1, 0))


class WordSearch(object):
    ___ __init__(self, puzzle):
        self.rows = puzzle.split()
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    ___ find_char(self, coordinate):
        __ coordinate.x < 0 or coordinate.x >= self.width:
            return
        __ coordinate.y < 0 or coordinate.y >= self.height:
            return
        return self.rows[coordinate.y][coordinate.x]

    ___ find(self, word, position, direction):
        current = copy.copy(position)
        for letter in word:
            __ self.find_char(current) != letter:
                return
            current += direction
        return position, current - direction

    ___ search(self, word):
        positions = (Point(x, y)
                     for x in range(self.width) for y in range(self.height))
        for pos in positions:
            for d in DIRECTIONS:
                result = self.find(word, pos, d)
                __ result:
                    return result
        return None
