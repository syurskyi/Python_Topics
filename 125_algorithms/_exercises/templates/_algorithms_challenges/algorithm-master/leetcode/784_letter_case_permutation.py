class Solution:
    ___ letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        __ not s:
            return ['']
        ans = []
        self.dfs(s, 0, ans, [])
        return ans

    ___ dfs(self, s, i, ans, path):
        __ i == len(s):
            ans.append(''.join(path))
            return

        options = [s[i]] __ s[i].isdigit() else [s[i].lower(), s[i].upper()]

        for c in options:
            path.append(c)
            self.dfs(s, i + 1, ans, path)
            path.pop()
