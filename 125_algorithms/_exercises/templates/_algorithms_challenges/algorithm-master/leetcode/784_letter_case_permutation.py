class Solution:
    ___ letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        __ n.. s:
            r.. ['']
        ans    # list
        self.dfs(s, 0, ans, [])
        r.. ans

    ___ dfs(self, s, i, ans, path):
        __ i __ l..(s):
            ans.a..(''.join(path))
            r..

        options = [s[i]] __ s[i].isdigit() ____ [s[i].lower(), s[i].upper()]

        ___ c __ options:
            path.a..(c)
            self.dfs(s, i + 1, ans, path)
            path.pop()
