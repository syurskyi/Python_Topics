class Solution:
    """
    @param: A: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    ___ combinationSum(self, A, target):
        ans    # list
        __ n.. A:
            r.. ans

        A.s..()
        self.dfs(A, 0, target, ans, [])
        r.. ans

    ___ dfs(self, A, start, remaining, ans, path):
        __ remaining __ 0:
            ans.a..(path[:])
            r..

        ___ i __ r..(start, l..(A)):
            __ remaining < A[i]:
                # note that, its `return` here
                # since `remaining < A[i]` and `A[i] <= A[i + 1] <= ...`
                # so once it continued, all iteration after i is no need
                r..

            path.a..(A[i])
            self.dfs(A, i, remaining - A[i], ans, path)
            path.pop()
