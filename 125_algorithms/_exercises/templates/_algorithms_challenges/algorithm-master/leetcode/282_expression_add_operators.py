"""
Main Concept:

in product case, needs to remove product in last recursion, and adds the product in current.
"""


class Solution:
    ___ addOperators(self, s, target
        """
        :type s: str
        :type target: int
        :rtype: List[str]
        """
        ans = []

        __ not s:
            r_ ans

        self.dfs(s, 0, target, 0, 0, ans, [])
        r_ ans

    ___ dfs(self, s, start, target, val, multi, ans, path
        __ start __ le.(s) and target __ val:
            ans.append(''.join(path))
            r_
        __ start >= le.(s
            r_

        for i in range(start, le.(s)):
            __ i > start and s[start] __ '0':
                # only allow i == start and its `0`
                break

            sa = s[start:i + 1]
            a = int(sa)

            __ start __ 0:
                self.dfs(s, i + 1, target, a, a, ans, [sa])
                continue

            self.dfs(s, i + 1, target, val + a, a, ans, path + ['+', sa])
            self.dfs(s, i + 1, target, val - a, -a, ans, path + ['-', sa])
            self.dfs(s, i + 1, target, val - multi + multi * a, multi * a, ans, path + ['*', sa])
