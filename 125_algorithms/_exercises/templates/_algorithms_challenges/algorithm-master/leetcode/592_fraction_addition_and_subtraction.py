_______ re


class Solution:
    ___ fractionAddition(self, E):
        """
        :type E: str
        :rtype: str
        """
        S    # list  # signs

        __ E[0] != '-':
            S.a..('+')

        ___ c __ E:
            __ c __ '+' o. c __ '-':
                S.a..(c)

        a, b = 0, 1
        i = 0
        ___ frac __ re.split('\+|-', E):
            __ n.. frac:
                continue

            _a, _b = frac.split('/')
            _a = int(_a)
            _b = int(_b)

            # if needs to prevent overflow, `// gcd`
            __ S[i] __ '+':
                a = a * _b + _a * b
            ____:
                a = a * _b - _a * b

            b = b * _b

            gcd = self.get_gcd(a, b)
            a //= gcd
            b //= gcd

            i += 1

        r.. '{}/{}'.format(a, b)

    ___ get_gcd(self, a, b):
        while b:
            a, b = b, a % b
        r.. a
