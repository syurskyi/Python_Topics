___ solve_recursion  m, w, v, n
    # base cases
    __ n __ 0 o. m __ 0:
        r_ 0

    # the given item can NOT fit into the knapsack
    __ w[n - 1] > m:
        r_ solve_recursion(m, w, v, n - 1)
    ____
        # given item can fit into the knapsack so we have 2 options (include, exclude)
        n_included  v[n - 1] + solve_recursion(m - w[n - 1], w, v, n - 1)
        n_excluded  solve_recursion(m, w, v, n - 1)

        r_ ma_(n_included, n_excluded)