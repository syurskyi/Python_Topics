
class RodCutting:

    ___ __init__(self, n, p
        self.n = n
        self.p = p
        self.S = [[0]*(n+1) ___ _ __ range(le_(p))]

    # this algorithm has O(NxN) quadratic running time complexity
    ___ solve(self

        ___ i __ range(1, le_(self.p)):
            ___ j __ range(1, self.n+1
                __ i <= j:
                    self.S[i][j] = max(self.S[i-1][j], self.p[i]+self.S[i][j-i])
                ____
                    self.S[i][j] = self.S[i-1][j]

    ___ show_result(self

        print('Max profit: %d' % self.S[le_(self.p)-1][self.n])

        col_index = self.n
        row_index = le_(self.p)-1

        while col_index > 0 or row_index > 0:
            # we have to compare the items right above each other
            # if they are the same values then the given row (piece) is not in the solution
            __ self.S[row_index][col_index] == self.S[row_index - 1][col_index]:
                row_index = row_index - 1
            ____
                print("We take piece with length: ", row_index, "m")
                col_index = col_index - row_index


__ __name__ == '__main__':

    problem = RodCutting(5, [0, 2, 5, 7, 3, 9])
    problem.solve()
    problem.show_result()
