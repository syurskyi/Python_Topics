class Point(object):
    ___ __init__(self, x, y):
        self.x = x
        self.y = y

    ___ __repr__(self):
        r.. 'Point({}:{})'.f..(self.x, self.y)

    ___ __add__(self, other):
        r.. Point(self.x + other.x, self.y + other.y)

    ___ __sub__(self, other):
        r.. Point(self.x - other.x, self.y - other.y)

    ___ __eq__(self, other):
        r.. self.x __ other.x a.. self.y __ other.y

    ___ __ne__(self, other):
        r.. n..(self __ other)


class WordSearch(object):
    ___ __init__(self, puzzle):
        pass

    ___ search(self, word):
        r.. N..
