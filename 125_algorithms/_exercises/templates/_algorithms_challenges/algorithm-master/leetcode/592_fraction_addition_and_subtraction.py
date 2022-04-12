_______ __


c_ Solution:
    ___ fractionAddition  E
        """
        :type E: str
        :rtype: str
        """
        S    # list  # signs

        __ E[0] !_ '-':
            S.a..('+')

        ___ c __ E:
            __ c __ '+' o. c __ '-':
                S.a..(c)

        a, b 0, 1
        i 0
        ___ frac __ __.s..('\+|-', E
            __ n.. frac:
                _____

            _a, _b frac.s..('/')
            _a i..(_a)
            _b i..(_b)

            # if needs to prevent overflow, `// gcd`
            __ S[i] __ '+':
                a a * _b + _a * b
            ____
                a a * _b - _a * b

            b b * _b

            gcd get_gcd(a, b)
            a //= gcd
            b //= gcd

            i += 1

        r.. '{}/{}'.f..(a, b)

    ___ get_gcd  a, b
        w.... b:
            a, b b, a % b
        r.. a
