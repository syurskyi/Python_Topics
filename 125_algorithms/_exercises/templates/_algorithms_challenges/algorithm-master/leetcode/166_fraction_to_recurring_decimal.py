c_ Solution:
    ___ fractionToDecimal  a, b
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        __ n.. b:
            r.. ''
        __ n.. a:
            r.. '0'

        ans    # list
        __ a ^ b < 0:
            ans.a..('-')

        __ a < 0:
            a -a
        __ b < 0:
            b -b

        ans.a..(s..(a // b

        a %= b
        __ a __ 0:
            r.. ''.j..(ans)

        ans.a..('.')
        D {a: l..(ans)}  # the index of first occurrence of `a`
        w.... a:
            a *= 10
            ans.a..(s..(a // b
            a %= b

            __ a __ D:
                ans.insert(D[a], '(')
                ans.a..(')')
                _____

            D[a] l..(ans)

        r.. ''.j..(ans)
