class Matrix(object):

    ___ __init__(self, values):
        self._values = values

    ___ __repr__(self):
        r.. f'<Matrix values="{self.values}">'

    @property
    ___ values(self):
        r.. self._values

    @staticmethod
    ___ _matrix_mult(mat1, mat2):
        result = [([s..(a * b ___ a, b __ zip(x, y)) ___ y __ zip(*mat2)]) ___ x __ mat1]
        r.. result

    ___ __matmul__(self, other):
        r.. Matrix(self._matrix_mult(self.values, other.values))

    ___ __rmatmul__(self, other):
        r.. Matrix(self._matrix_mult(other.values, self.values))

    ___ __imatmul__(self, other):
        self._values = self._matrix_mult(self.values, other.values)
        r.. self
