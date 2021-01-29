
c_ RodCutting:

    ___  -   n, p
        n = n
        p = p
        S = [[0]*(n+1) ___ _ __ ra__(le_(p))]

    # this algorithm has O(NxN) quadratic running time complexity
    ___ solve(self

        ___ i __ ra__(1, le_(p)):
            ___ j __ ra__(1, n+1
                __ i <= j:
                    S[i][j] = ma_(S[i-1][j], p[i]+S[i][j-i])
                ____
                    S[i][j] = S[i-1][j]

    ___ show_result(self

        print('Max profit: %d' % S[le_(p)-1][n])

        col_index = n
        row_index = le_(p)-1

        w__ col_index > 0 or row_index > 0:
            # we have to compare the items right above each other
            # if they are the same values then the given row (piece) is not in the solution
            __ S[row_index][col_index] __ S[row_index - 1][col_index]:
                row_index = row_index - 1
            ____
                print("We take piece with length: ", row_index, "m")
                col_index = col_index - row_index


__ ___ __ '__main__':

    problem = RodCutting(5, [0, 2, 5, 7, 3, 9])
    problem.solve()
    problem.show_result()
