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

    ___ dfs  words, n, ans, p..
        __ (l..(p..) __ n a..
            is_valid(p..)):
            ans.a..(p.. | )
            r..

        __ l..(p..) >= n:
            r..

        ___ i __ r..(l..(words)):
            p...a..(words[i])
            dfs(words, n, ans, p..)
            p...pop()

    ___ is_valid  p..
        __ n.. p.. o. l..(p..) != l..(p..[0]
            r.. F..

        ___ i __ r..(1, l..(p..)):
            ___ j __ r..(i
                __ p..[i][j] != p..[j][i]:
                    r.. F..

        r.. T..
