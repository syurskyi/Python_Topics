class Matrix(object):
    ___ __init__(self, s):
        self.rows = [[int(n) for n in row.split()]
                     for row in s.split('\n')]

    @property
    ___ columns(self):
        return [list(tup) for tup in zip(*self.rows)]
