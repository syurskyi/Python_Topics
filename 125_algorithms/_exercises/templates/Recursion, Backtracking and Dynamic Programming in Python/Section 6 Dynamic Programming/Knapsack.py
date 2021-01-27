
class KnapsackProblem:

    ___ __init__(self, n, M, w, v
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 ___ _ __ range(M+1)] ___ _ __ range(n+1)]

    ___ solve(self
        # construct the S dynamic programming table
        # O(n*M)
        ___ i __ range(self.n+1
            ___ w __ range(self.M+1
                not_taking_item = self.S[i - 1][w]
                taking_item = 0

                __ self.w[i] <= w:
                    taking_item = self.v[i] + self.S[i - 1][w - self.w[i]]

                # memoization - we store the sub-results to avoid recalculating the same values
                self.S[i][w] = max(not_taking_item, taking_item)

    ___ show_result(self

        print("Total benefit: %d" % self.S[self.n][self.M])

        w = self.M
        ___ n __ range(self.n, 0, -1
            __ self.S[n][w] != 0 and self.S[n][w] != self.S[n - 1][w]:
                print("We take item #%d" % n)
                w = w - self.w[n]


__ __name__ == '__main__':

    num_of_items = 4
    knapsack_capacity = 7
    weights = [0, 1, 3, 4, 5]
    profits = [0, 1, 4, 5, 7]
    knapsack = KnapsackProblem(num_of_items, knapsack_capacity, weights, profits)
    knapsack.solve()
    knapsack.show_result()

