"""
DFS
"""
class Solution:
    """
    @param: A: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    ___ subsetsWithDup(self, A):
        __ n.. A:
            r.. [[]]

        ans    # list
        self.dfs(s..(A), 0, ans, [])
        r.. ans

    ___ dfs(self, A, start, ans, subset):
        ans.a..(subset[:])

        __ start >= l..(A):
            r..

        ___ i __ r..(start, l..(A)):
            __ i - 1 >= start and A[i] __ A[i - 1]:
                continue

            self.dfs(A, i + 1, ans, subset + [A[i]])

            """
            backtracking if using same list
            """
            # subset.append(A[i])
            # self.dfs(A, i + 1, ans, subset)
            # subset.pop()
