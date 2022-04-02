"""
Premium question
Non-dp version of edit distance
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ isOneEditDistance  s, t
        """
        String

        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = l..(s), l..(t)
        __ m > n: r.. isOneEditDistance(t, s)
        __ n-m > 1: r.. F..

        diff = 0
        i, j = 0, 0
        w.... i < m a.. j < n a.. diff < 2:
            __ s[i] __ t[j]:
                i += 1
                j += 1
            ____:
                __ m != n:
                    j += 1  # delete
                ____:  # replace s[i]
                    i += 1
                    j += 1

                diff += 1

        r.. diff __ 1 o. diff __ 0 a.. m != n


c_ Solution1(o..
    ___ isOneEditDistance  s, t
        """
        Iterator version
        """
        m, n = l..(s), l..(t)
        __ m > n: r.. isOneEditDistance(t, s)
        __ n-m > 1: r.. F..

        diff = 0
        i, j = i..(s), i..(t)
        a, b = next(i, N..), next(j, N..)
        w.... a a.. b a.. diff < 2:
            __ a __ b:
                a, b = next(i, N..), next(j, N..)
            ____:
                __ m != n:
                    b = next(j, N..)
                ____:
                    a, b = next(i, N..), next(j, N..)

                diff += 1

        r.. diff __ 1 o. diff __ 0 a.. m != n
