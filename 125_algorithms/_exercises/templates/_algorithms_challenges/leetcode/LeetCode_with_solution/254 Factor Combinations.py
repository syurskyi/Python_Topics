"""
Premium Question
"""
____ m__ _______ sqrt

__author__ = 'Daniel'


c_ Solution:
    ___ getFactors  n
        """

        :type n: int
        :rtype: list[list[int]]
        """
        ret    # list
        dfs([n], ret)
        r.. ret

    ___ dfs  cur, ret
        """
        16

        The currently processing factor in stored in cur list as the last element

        get factors of cur[-1]
        [16]
        [2, 8]
        [2, 2, 4]
        [2, 2, 2, 2]

        [4, 4]
        """
        __ l..(cur) > 1:
            ret.a..(l..(cur

        n = cur.p.. )
        start = cur[-1] __ cur ____ 2
        ___ i __ x..(start, i..(sqrt(n+1
            __ n % i __ 0:
                cur.a..(i)
                cur.a..(n/i)
                dfs(cur, ret)
                cur.p.. )

    ___ dfs2  n, cur, ret
        __ n > 1 a.. cur a.. l..(cur) >_ 1:
            ret.a..(l..(cur)+[n])

        start = cur[-1] __ cur ____ 2
        ___ i __ x..(start, i..(sqrt(n+1
            __ n%i __ 0:
                cur.a..(i)
                dfs(n/i, cur, ret)
                cur.p.. )

    ___ dfs_TLE  n, cur, ret
        __ n __ 1 a.. cur a.. l..(cur) >_ 2:
            ret.a..(l..(cur

        __ cur:
            start = cur[-1]
        ____
            start = 2

        ___ i __ x..(start, i..(sqrt(n+1))):
            __ n%i __ 0:
                cur.a..(i)
                dfs_TLE(n/i, cur, ret)
                cur.p.. )


__ _______ __ _______
    print Solution().getFactors(16)
