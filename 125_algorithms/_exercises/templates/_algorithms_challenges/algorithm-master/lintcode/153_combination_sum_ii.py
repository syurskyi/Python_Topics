class Solution:
    """
    @param: A: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    ___ combinationSum2(self, A, target):
        ans    # list
        __ n.. A:
            r.. ans

        A.sort()
        self.dfs(A, 0, target, ans, [])
        r.. ans

    ___ dfs(self, A, start, remaining, ans, path):
        __ remaining __ 0:
            ans.a..(path[:])
            r..

        ___ i __ r..(start, l..(A)):
            __ remaining < A[i]:
                r..

            # to prevent [1', 2, 5] and [1", 2, 5]
            # appear in result at same time
            __ i > start and A[i] __ A[i - 1]:
                continue

            path.a..(A[i])
            self.dfs(A, i + 1, remaining - A[i], ans, path)
            path.pop()
