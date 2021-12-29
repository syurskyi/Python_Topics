import re


class Solution:
    ___ fractionAddition(self, E):
        """
        :type E: str
        :rtype: str
        """
        S = []  # signs

        __ E[0] != '-':
            S.append('+')

        for c in E:
            __ c == '+' or c == '-':
                S.append(c)

        a, b = 0, 1
        i = 0
        for frac in re.split('\+|-', E):
            __ not frac:
                continue

            _a, _b = frac.split('/')
            _a = int(_a)
            _b = int(_b)

            # if needs to prevent overflow, `// gcd`
            __ S[i] == '+':
                a = a * _b + _a * b
            else:
                a = a * _b - _a * b

            b = b * _b

            gcd = self.get_gcd(a, b)
            a //= gcd
            b //= gcd

            i += 1

        return '{}/{}'.format(a, b)

    ___ get_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
