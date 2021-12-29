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
        return not(self == other)


class WordSearch(object):
    ___ __init__(self, puzzle):
        pass

    ___ search(self, word):
        return None
