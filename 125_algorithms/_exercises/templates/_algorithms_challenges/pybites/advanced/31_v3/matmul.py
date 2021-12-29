class Matrix(object):

    ___ __init__(self, values):
        self.values = values

    ___ __repr__(self):
        return f'<Matrix values="{self.values}">'

    ___ __matmul__(self, other):
        A = self.values
        B = list(zip(*other.values))
        print(A)
        print(B)
        Y = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                Y[i][j] = sum(a * b for a, b in zip(A[i], B[j]))
        return Matrix(Y)

    ___ __imatmul__(self, other):
        Y = self @ other
        self.values = Y.values
        return self

    ___ __rmatmul__(self, other):
        return self @ other
