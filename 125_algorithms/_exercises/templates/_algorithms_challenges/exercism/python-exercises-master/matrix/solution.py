class Matrix(object
    ___ __init__(self, s
        self.rows = [[int(n) ___ n in row.split()]
                     ___ row in s.split('\n')]

    @property
    ___ columns(self
        r_ [list(tup) ___ tup in zip(*self.rows)]
