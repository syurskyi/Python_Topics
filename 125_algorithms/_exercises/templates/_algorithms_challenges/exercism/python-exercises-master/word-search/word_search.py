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
        r_ not(self __ other)


class WordSearch(object
    ___ __init__(self, puzzle
        pass

    ___ search(self, word
        r_ None
