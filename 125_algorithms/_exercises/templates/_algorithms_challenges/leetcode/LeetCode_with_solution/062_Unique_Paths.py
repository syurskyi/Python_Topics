c_ Solution:
    ___ uniquePaths  m, n
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dmap = [[0] * n ___ _ __ r.. m)]
        ___ i __ r.. m
            dmap[i][0] = 1
        ___ j __ r.. n
            dmap[0][j] = 1
        ___ i __ r.. 1, m
            ___ j __ r.. 1, n
                l = u = 0
                __ i-1 >= 0:
                    u = dmap[i-1][j]
                __ j-1>= 0:
                    l = dmap[i][j-1]
                dmap[i][j] = l + u
        r_ dmap[m-1][n-1]
