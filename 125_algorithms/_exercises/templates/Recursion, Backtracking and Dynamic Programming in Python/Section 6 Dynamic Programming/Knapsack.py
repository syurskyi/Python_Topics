
c_ KnapsackProblem:

    ___  -   n, M, w, v
        n = n
        M = M
        w = w
        v = v
        S = [[0 ___ _ __ ra__(M+1)] ___ _ __ ra__(n+1)]

    ___ solve(self
        # construct the S dynamic programming table
        # O(n*M)
        ___ i __ ra__(n+1
            ___ w __ ra__(M+1
                not_taking_item = S[i - 1][w]
                taking_item = 0

                __ w[i] <= w:
                    taking_item = v[i] + S[i - 1][w - w[i]]

                # memoization - we store the sub-results to avoid recalculating the same values
                S[i][w] = max(not_taking_item, taking_item)

    ___ show_result(self

        print("Total benefit: %d" % S[n][M])

        w = M
        ___ n __ ra__(n, 0, -1
            __ S[n][w] != 0 a__ S[n][w] != S[n - 1][w]:
                print("We take item #%d" % n)
                w = w - w[n]


__ ___ __ '__main__':

    num_of_items = 4
    knapsack_capacity = 7
    weights = [0, 1, 3, 4, 5]
    profits = [0, 1, 4, 5, 7]
    knapsack = KnapsackProblem(num_of_items, knapsack_capacity, weights, profits)
    knapsack.solve()
    knapsack.show_result()

