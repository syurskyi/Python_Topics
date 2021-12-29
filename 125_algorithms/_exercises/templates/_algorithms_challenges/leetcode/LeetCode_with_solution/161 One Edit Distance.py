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
        m, n = len(s), len(t)
        __ m > n: return self.isOneEditDistance(t, s)
        __ n-m > 1: return False

        diff = 0
        i, j = 0, 0
        while i < m and j < n and diff < 2:
            __ s[i] == t[j]:
                i += 1
                j += 1
            else:
                __ m != n:
                    j += 1  # delete
                else:  # replace s[i]
                    i += 1
                    j += 1

                diff += 1

        return diff == 1 or diff == 0 and m != n


class Solution1(object):
    ___ isOneEditDistance(self, s, t):
        """
        Iterator version
        """
        m, n = len(s), len(t)
        __ m > n: return self.isOneEditDistance(t, s)
        __ n-m > 1: return False

        diff = 0
        i, j = iter(s), iter(t)
        a, b = next(i, None), next(j, None)
        while a and b and diff < 2:
            __ a == b:
                a, b = next(i, None), next(j, None)
            else:
                __ m != n:
                    b = next(j, None)
                else:
                    a, b = next(i, None), next(j, None)

                diff += 1

        return diff == 1 or diff == 0 and m != n
