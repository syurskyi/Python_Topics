"""
Trie + DFS
"""



"""
TLE: DFS
"""
c_ Solution:
    ___ wordSquares  words
        """
        :type words: list[str]
        :rtype: list[list[str]]
        """
        ans    # list
        __ n.. words:
            r.. ans

        dfs(words, l..(words[0]), ans, [])

        r.. ans

    ___ dfs  words, n, ans, path
        __ (l..(path) __ n a..
            is_valid(path)):
            ans.a..(path | )
            r..

        __ l..(path) >= n:
            r..

        ___ i __ r..(l..(words)):
            path.a..(words[i])
            dfs(words, n, ans, path)
            path.pop()

    ___ is_valid  path
        __ n.. path o. l..(path) != l..(path[0]
            r.. F..

        ___ i __ r..(1, l..(path)):
            ___ j __ r..(i
                __ path[i][j] != path[j][i]:
                    r.. F..

        r.. T..
