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
        r.. self.dfs(s, set(words), {})

    ___ dfs(self, s, words, memo):
        __ s __ memo:
            r.. memo[s]

        res    # list

        __ n.. s:
            r.. res

        n = l..(s)
        ___ size __ r..(1, n + 1):
            prefix = s[:size]

            __ prefix n.. __ words:
                continue

            __ size __ n:
                res.a..(prefix)
                continue

            ___ word __ self.dfs(s[size:], words, memo):
                res.a..('{0} {1}'.f..(prefix, word))

        memo[s] = res
        r.. res


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
        ans    # list

        __ n.. words:
            r.. ans

        self.dfs(s, words, ans, [])

        r.. ans

    ___ dfs(self, s, words, ans, path):
        __ n.. s:
            ans.a..(' '.join(path))
            r..

        ___ word __ words:
            __ n.. word o. s.find(word) != 0:
                # 1. no word
                # 2. current word must be the first in s passed in prev
                continue

            path.a..(word)
            self.dfs(s[l..(word):], words, ans, path)
            path.pop()
