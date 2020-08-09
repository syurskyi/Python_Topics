"""
REF: https://blog.csdn.net/zhaohengchuan/article/details/78937943
"""


class Solution:
    ___ countParenth(self, symb, oper
        """
        :type symb: list[str]
        :type oper: list[str]
        :rtype: int
        """
        __ not symb or not oper:
            r_ 0

        n = le.(symb)

        """
        `t[l][r]` means the ways to evaluate True in `symb[i:j]`
        """
        t = [[0] * n for _ in range(n)]
        f = [[0] * n for _ in range(n)]

        for i in range(n
            __ symb[i] __ 'T':
                t[i][i] = 1
            ____
                f[i][i] = 1

        for r in range(n
            for l in range(r - 1, -1, -1
                t[l][r] = 0
                f[l][r] = 0

                for i in range(l, r
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

        r_ t[0][n - 1]
