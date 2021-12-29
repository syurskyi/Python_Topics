"""
DFS
"""
class Solution:
    """
    @param: A: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    ___ subsetsWithDup(self, A):
        __ not A:
            return [[]]

        ans = []
        self.dfs(sorted(A), 0, ans, [])
        return ans

    ___ dfs(self, A, start, ans, subset):
        ans.append(subset[:])

        __ start >= len(A):
            return

        for i in range(start, len(A)):
            __ i - 1 >= start and A[i] == A[i - 1]:
                continue

            self.dfs(A, i + 1, ans, subset + [A[i]])

            """
            backtracking if using same list
            """
            # subset.append(A[i])
            # self.dfs(A, i + 1, ans, subset)
            # subset.pop()
