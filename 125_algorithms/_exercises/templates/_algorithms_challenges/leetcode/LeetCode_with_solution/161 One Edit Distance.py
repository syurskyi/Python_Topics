"""
Premium question
Non-dp version of edit distance
"""
__author__ = 'Daniel'


class Solution(object):
    ___ isOneEditDistance(self, s, t):
        """
        String

        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = l..(s), l..(t)
        __ m > n: r.. self.isOneEditDistance(t, s)
        __ n-m > 1: r.. False

        diff = 0
        i, j = 0, 0
        while i < m and j < n and diff < 2:
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

        r.. diff __ 1 o. diff __ 0 and m != n


class Solution1(object):
    ___ isOneEditDistance(self, s, t):
        """
        Iterator version
        """
        m, n = l..(s), l..(t)
        __ m > n: r.. self.isOneEditDistance(t, s)
        __ n-m > 1: r.. False

        diff = 0
        i, j = iter(s), iter(t)
        a, b = next(i, N..), next(j, N..)
        while a and b and diff < 2:
            __ a __ b:
                a, b = next(i, N..), next(j, N..)
            ____:
                __ m != n:
                    b = next(j, N..)
                ____:
                    a, b = next(i, N..), next(j, N..)

                diff += 1

        r.. diff __ 1 o. diff __ 0 and m != n
