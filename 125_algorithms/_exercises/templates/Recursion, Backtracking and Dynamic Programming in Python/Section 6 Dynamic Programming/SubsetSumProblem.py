
class SubsetSumProblem:

    ___ __init__(self, nums, m
        self.nums = nums
        self.m = m
        self.S = [[False ___ _ __ range(m+1)] ___ _ __ range(le_(nums)+1)]

    ___ solve(self

        # initialize the first row and first column
        ___ i __ range(le_(self.nums) + 1
            self.S[i][0] = True

        # we have to construct the table with the cells one by one
        ___ i __ range(1, le_(self.nums) + 1
            ___ j __ range(1, self.m + 1
                __ j < self.nums[i-1]:
                    self.S[i][j] = self.S[i-1][j]
                ____
                    __ self.S[i - 1][j]:
                        # this is when we do NOT include the given item rowIndex
                        self.S[i][j] = self.S[i - 1][j]
                    ____
                        # do include the item i
                        self.S[i][j] = self.S[i - 1][j - self.nums[i - 1]]

    ___ show_result(self

        print("The problem is feasible: %s" % self.S[le_(self.nums)][self.m])

        __ not self.S[le_(self.nums)][self.m]:
            r_

        # print out the items in the subset
        col_index = self.m
        row_index = le_(self.nums)

        while col_index > 0 or row_index > 0:
            __ self.S[row_index][col_index] == self.S[row_index - 1][col_index]:
                row_index = row_index - 1
            ____
                print('We take item: %d' % self.nums[row_index - 1])
                col_index = col_index - self.nums[row_index - 1]
                row_index = row_index - 1


__ __name__ == '__main__':

    M = 11
    n = [1, 2, 5, 3]

    problem = SubsetSumProblem(n, M)
    problem.solve()
    problem.show_result()
