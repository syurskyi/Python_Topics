"""
REF: https://blog.csdn.net/zhaohengchuan/article/details/78937943
"""


c_ Solution:
    ___ countParenth  symb, oper):
        """
        :type symb: list[str]
        :type oper: list[str]
        :rtype: int
        """
        __ n.. symb o. n.. oper:
            r.. 0

        n = l..(symb)

        """
        `t[l][r]` means the ways to evaluate True in `symb[i:j]`
        """
        t = [[0] * n ___ _ __ r..(n)]
        f = [[0] * n ___ _ __ r..(n)]

        ___ i __ r..(n):
            __ symb[i] __ 'T':
                t[i][i] = 1
            ____:
                f[i][i] = 1

        ___ r __ r..(n):
            ___ l __ r..(r - 1, -1, -1):
                t[l][r] = 0
                f[l][r] = 0

                ___ i __ r..(l, r):
                    __ oper[i] __ '&':
                        t[l][r] += t[l][i] * t[i + 1][r]
                        f[l][r] += (
                            (t[l][i] + f[l][i]) *
                            (t[i + 1][r] + f[i + 1][r]) -
                            t[l][i] * t[i + 1][r]
                        )
                    ____ oper[i] __ '|':
                        t[l][r] += (
                            (t[l][i] + f[l][i]) *
                            (t[i + 1][r] + f[i + 1][r]) -
                            f[l][i] * f[i + 1][r]
                        )
                        f[l][r] += f[l][i] * f[i + 1][r]
                    ____ oper[i] __ '^':
                        t[l][r] += t[l][i] * f[i + 1][r] + f[l][i] * t[i + 1][r]
                        f[l][r] += t[l][i] * t[i + 1][r] + f[l][i] * f[i + 1][r]

        r.. t[0][n - 1]
