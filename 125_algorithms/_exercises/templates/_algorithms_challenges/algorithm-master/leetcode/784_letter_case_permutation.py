class Solution:
    ___ letterCasePermutation(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        __ not s:
            r_ ['']
        ans = []
        self.dfs(s, 0, ans, [])
        r_ ans

    ___ dfs(self, s, i, ans, path
        __ i __ le.(s
            ans.append(''.join(path))
            r_

        options = [s[i]] __ s[i].isdigit() else [s[i].lower(), s[i].upper()]

        for c in options:
            path.append(c)
            self.dfs(s, i + 1, ans, path)
            path.pop()
