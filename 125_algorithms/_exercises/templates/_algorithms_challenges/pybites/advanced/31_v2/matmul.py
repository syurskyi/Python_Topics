c_ Matrix(o..

    ___ - , values
        _values values

    ___  -r
        r.. f'<Matrix values="{values}">'

    $
    ___ values
        r.. _values

    $
    ___ _matrix_mult(mat1, mat2
        result [([s..(a * b ___ a, b __ z..(x, y ___ y __ z..(*mat2)]) ___ x __ mat1]
        r.. result

    ___ __matmul__  other
        r.. Matrix(_matrix_mult(values, other.values

    ___ __rmatmul__  other
        r.. Matrix(_matrix_mult(other.values, values

    ___ __imatmul__  other
        _values _matrix_mult(values, other.values)
        r.. _
