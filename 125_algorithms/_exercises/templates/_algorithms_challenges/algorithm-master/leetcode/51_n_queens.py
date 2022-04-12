c_ Solution:
    ___ solveNQueens  n
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans    # list
        __ n.. n:
            r.. ans

        G [['.'  * n ___ _ __ r..(n)]
        dfs(G, 0, ans)
        r.. ans

    ___ dfs  G, y, ans
        __ y __ l..(G
            ans.a..(clone_board(G
            r..

        ___ x __ r..(l..(G:
            __ is_valid(G, x, y
                G[x][y] 'Q'
                dfs(G, y + 1, ans)
                G[x][y] '.'

    ___ is_valid  G, x, y
        """
        traverse left half => i in [0, n], j in [0, y - 1] to
        1. avoid `j == y` and speed up
        and return False if
        2. `x == i` => at same row
        3. `x - i = y - j` => `x + j = y + i` => left diagonal line
        4. `x - i = -(y - j)` => `x + y = i + j` => right diagonal line
        """
        ___ i __ r..(l..(G:
            ___ j __ r..(y
                __ G[i][j] !_ 'Q':
                    _____
                __ (x + j __ y + i o.
                    x + y __ i + j o.
                    x __ i
                    r.. F..
        r.. T..

    ___ clone_board  G
        res    # list
        ___ R __ G:
            res.a..(''.j..(R
        r.. res
