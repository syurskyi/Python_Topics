class Solution:
    """
    dfs/dp: optimized by memory searching
    """
    ___ wordBreak(self, s, words):
        """
        :type s: str
        :type words: list[str]
        :rtype: list[str]
        """
        return self.dfs(s, set(words), {})

    ___ dfs(self, s, words, memo):
        __ s in memo:
            return memo[s]

        res = []

        __ not s:
            return res

        n = len(s)
        for size in range(1, n + 1):
            prefix = s[:size]

            __ prefix not in words:
                continue

            __ size == n:
                res.append(prefix)
                continue

            for word in self.dfs(s[size:], words, memo):
                res.append('{0} {1}'.format(prefix, word))

        memo[s] = res
        return res


class Solution:
    """
    dfs: TLE

    bad in edge case:
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    """
    ___ wordBreak(self, s, words):
        """
        :type s: str
        :type words: list[str]
        :rtype: list[str]
        """
        ans = []

        __ not words:
            return ans

        self.dfs(s, words, ans, [])

        return ans

    ___ dfs(self, s, words, ans, path):
        __ not s:
            ans.append(' '.join(path))
            return

        for word in words:
            __ not word or s.find(word) != 0:
                # 1. no word
                # 2. current word must be the first in s passed in prev
                continue

            path.append(word)
            self.dfs(s[len(word):], words, ans, path)
            path.pop()
