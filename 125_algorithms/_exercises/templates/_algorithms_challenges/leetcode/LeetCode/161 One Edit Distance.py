"""
Premium question
Non-dp version of edit distance
"""
__author__ = 'Daniel'


class Solution(object
    ___ isOneEditDistance(self, s, t
        """
        String

        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = le.(s), le.(t)
        __ m > n: r_ self.isOneEditDistance(t, s)
        __ n-m > 1: r_ False

        diff = 0
        i, j = 0, 0
        w___ i < m and j < n and diff < 2:
            __ s[i] __ t[j]:
                i += 1
                j += 1
            ____
                __ m != n:
                    j += 1  # delete
                ____  # replace s[i]
                    i += 1
                    j += 1

                diff += 1

        r_ diff __ 1 or diff __ 0 and m != n


class Solution1(object
    ___ isOneEditDistance(self, s, t
        """
        Iterator version
        """
        m, n = le.(s), le.(t)
        __ m > n: r_ self.isOneEditDistance(t, s)
        __ n-m > 1: r_ False

        diff = 0
        i, j = iter(s), iter(t)
        a, b = next(i, None), next(j, None)
        w___ a and b and diff < 2:
            __ a __ b:
                a, b = next(i, None), next(j, None)
            ____
                __ m != n:
                    b = next(j, None)
                ____
                    a, b = next(i, None), next(j, None)

                diff += 1

        r_ diff __ 1 or diff __ 0 and m != n
