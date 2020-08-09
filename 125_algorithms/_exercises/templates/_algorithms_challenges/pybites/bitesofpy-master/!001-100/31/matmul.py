class Matrix(object

    ___ __init__(self, values
        self._values = values

    ___ __repr__(self
        r_ f'<Matrix values="{self.values}">'

    @property
    ___ values(self
        r_ self._values

    @staticmethod
    ___ _matrix_mult(mat1, mat2
        result = [([su.(a * b ___ a, b in zip(x, y)) ___ y in zip(*mat2)]) ___ x in mat1]
        r_ result

    ___ __matmul__(self, other
        r_ Matrix(self._matrix_mult(self.values, other.values))

    ___ __rmatmul__(self, other
        r_ Matrix(self._matrix_mult(other.values, self.values))

    ___ __imatmul__(self, other
        self._values = self._matrix_mult(self.values, other.values)
        r_ self
