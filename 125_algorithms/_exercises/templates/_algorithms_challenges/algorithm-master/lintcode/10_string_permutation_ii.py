class Solution:
    """
    @param: S: A string
    @return: all permutations
    """
    ___ stringPermutation2(self, S
        __ not S:
            r_ ['']

        S = sorted(S)

        ans = []
        self.dfs(S, ans, [])
        r_ ans

    ___ dfs(self, S, ans, path
        __ not S:
            ans.append(''.join(path))
            r_

        for i in range(le.(S)):
            __ i > 0 and S[i] __ S[i - 1]:
                continue
            path.append(S[i])
            self.dfs(S[:i] + S[i + 1:], ans, path)
            path.pop()
