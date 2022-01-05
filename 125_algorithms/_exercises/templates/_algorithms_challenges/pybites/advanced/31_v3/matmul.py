c_ Matrix(object):

    ___ - , values):
        values = values

    ___ __repr__
        r.. f'<Matrix values="{values}">'

    ___ __matmul__  other):
        A = values
        B = l..(z..(*other.values))
        print(A)
        print(B)
        Y = [[0 ___ _ __ r..(l..(B))] ___ _ __ r..(l..(A))]
        ___ i __ r..(l..(A)):
            ___ j __ r..(l..(B)):
                Y[i][j] = s..(a * b ___ a, b __ z..(A[i], B[j]))
        r.. Matrix(Y)

    ___ __imatmul__  other):
        Y = self @ other
        values = Y.values
        r.. self

    ___ __rmatmul__  other):
        r.. self @ other
