___ solve_recursion(self, m, w, v, n
    # base cases
    __ n == 0 or m == 0:
        r_ 0

    # the given item can NOT fit into the knapsack
    __ w[n - 1] > m:
        r_ self.solve_recursion(m, w, v, n - 1)
    ____
        # given item can fit into the knapsack so we have 2 options (include, exclude)
        n_included = v[n - 1] + self.solve_recursion(m - w[n - 1], w, v, n - 1)
        n_excluded = self.solve_recursion(m, w, v, n - 1)

        r_ max(n_included, n_excluded)