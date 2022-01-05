c_ Solution:
    """
    dfs/dp: optimized by memory searching
    """
    ___ wordBreak  s, words):
        """
        :type s: str
        :type words: list[str]
        :rtype: list[str]
        """
        r.. dfs(s, set(words), {})

    ___ dfs  s, words, memo):
        __ s __ memo:
            r.. memo[s]

        res    # list

        __ n.. s:
            r.. res

        n = l..(s)
        ___ size __ r..(1, n + 1):
            prefix = s[:size]

            __ prefix n.. __ words:
                _____

            __ size __ n:
                res.a..(prefix)
                _____

            ___ word __ dfs(s[size:], words, memo):
                res.a..('{0} {1}'.f..(prefix, word))

        memo[s] = res
        r.. res


c_ Solution:
    """
    dfs: TLE

    bad in edge case:
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    """
    ___ wordBreak  s, words):
        """
        :type s: str
        :type words: list[str]
        :rtype: list[str]
        """
        ans    # list

        __ n.. words:
            r.. ans

        dfs(s, words, ans, [])

        r.. ans

    ___ dfs  s, words, ans, path):
        __ n.. s:
            ans.a..(' '.j..(path))
            r..

        ___ word __ words:
            __ n.. word o. s.find(word) != 0:
                # 1. no word
                # 2. current word must be the first in s passed in prev
                _____

            path.a..(word)
            dfs(s[l..(word):], words, ans, path)
            path.pop()
