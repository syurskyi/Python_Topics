class Solution:
    """
    @param: A: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    ___ combinationSum(self, A, target):
        ans = []
        __ not A:
            return ans

        A.sort()
        self.dfs(A, 0, target, ans, [])
        return ans

    ___ dfs(self, A, start, remaining, ans, path):
        __ remaining == 0:
            ans.append(path[:])
            return

        for i in range(start, len(A)):
            __ remaining < A[i]:
                # note that, its `return` here
                # since `remaining < A[i]` and `A[i] <= A[i + 1] <= ...`
                # so once it continued, all iteration after i is no need
                return

            path.append(A[i])
            self.dfs(A, i, remaining - A[i], ans, path)
            path.pop()
