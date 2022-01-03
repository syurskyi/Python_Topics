c_ Matrix(object):

    ___ - , values):
        _values = values

    ___ __repr__
        r.. f'<Matrix values="{values}">'

    $
    ___ values
        r.. _values

    @staticmethod
    ___ _matrix_mult(mat1, mat2):
        result = [([s..(a * b ___ a, b __ z..(x, y)) ___ y __ z..(*mat2)]) ___ x __ mat1]
        r.. result

    ___ __matmul__(self, other):
        r.. Matrix(_matrix_mult(values, other.values))

    ___ __rmatmul__(self, other):
        r.. Matrix(_matrix_mult(other.values, values))

    ___ __imatmul__(self, other):
        _values = _matrix_mult(values, other.values)
        r.. self
