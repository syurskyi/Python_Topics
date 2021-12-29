class Matrix(object):

    ___ __init__(self, values):
        self.values = values

    ___ __repr__(self):
        r.. f'<Matrix values="{self.values}">'

    ___ __matmul__(self, other):
        A = self.values
        B = l..(zip(*other.values))
        print(A)
        print(B)
        Y = [[0 ___ _ __ r..(l..(B))] ___ _ __ r..(l..(A))]
        ___ i __ r..(l..(A)):
            ___ j __ r..(l..(B)):
                Y[i][j] = s..(a * b ___ a, b __ zip(A[i], B[j]))
        r.. Matrix(Y)

    ___ __imatmul__(self, other):
        Y = self @ other
        self.values = Y.values
        r.. self

    ___ __rmatmul__(self, other):
        r.. self @ other
