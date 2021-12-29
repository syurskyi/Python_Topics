class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        A = self.values
        B = list(zip(*other.values))
        print(A)
        print(B)
        Y = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                Y[i][j] = sum(a * b for a, b in zip(A[i], B[j]))
        return Matrix(Y)

    def __imatmul__(self, other):
        Y = self @ other
        self.values = Y.values
        return self

    def __rmatmul__(self, other):
        return self @ other
