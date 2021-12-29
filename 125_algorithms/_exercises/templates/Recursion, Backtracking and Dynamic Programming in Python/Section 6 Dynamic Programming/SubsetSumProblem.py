
c_ SubsetSumProblem:

    ___  -   nums, m
        nums  nums
        m  m
        S  [[F.. ___ _ __ ra__(m+1)] ___ _ __ ra__(le_(nums)+1)]

    ___ solve(self

        # initialize the first row and first column
        ___ i __ ra__(le_(nums) + 1
            S[i][0]  T..

        # we have to construct the table with the cells one by one
        ___ i __ ra__(1, le_(nums) + 1
            ___ j __ ra__(1, m + 1
                __ j < nums[i-1]:
                    S[i][j]  S[i-1][j]
                ____
                    __ S[i - 1][j]:
                        # this is when we do NOT include the given item rowIndex
                        S[i][j]  S[i - 1][j]
                    ____
                        # do include the item i
                        S[i][j]  S[i - 1][j - nums[i - 1]]

    ___ show_result(self

        print("The problem is feasible: %s" % S[le_(nums)][m])

        __ no. S[le_(nums)][m]:
            r_

        # print out the items in the subset
        col_index  m
        row_index  le_(nums)

        w__ col_index > 0 or row_index > 0:
            __ S[row_index][col_index] __ S[row_index - 1][col_index]:
                row_index  row_index - 1
            ____
                print('We take item: %d' % nums[row_index - 1])
                col_index  col_index - nums[row_index - 1]
                row_index  row_index - 1


__ ___ __ '__main__':

    M  11
    n  [1, 2, 5, 3]

    problem  SubsetSumProblem(n, M)
    problem.solve()
    problem.show_result()
