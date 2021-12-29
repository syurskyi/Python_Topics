class Solution:
    """
    @param: S: A string
    @return: all permutations
    """
    ___ stringPermutation2(self, S):
        __ n.. S:
            r.. ['']

        S = s..(S)

        ans    # list
        self.dfs(S, ans, [])
        r.. ans

    ___ dfs(self, S, ans, path):
        __ n.. S:
            ans.a..(''.join(path))
            r..

        ___ i __ r..(l..(S)):
            __ i > 0 and S[i] __ S[i - 1]:
                continue
            path.a..(S[i])
            self.dfs(S[:i] + S[i + 1:], ans, path)
            path.pop()
