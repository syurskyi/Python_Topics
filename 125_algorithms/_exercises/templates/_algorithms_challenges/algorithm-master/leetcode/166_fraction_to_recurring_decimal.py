class Solution:
    ___ fractionToDecimal(self, a, b):
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
            a = -a
        __ b < 0:
            b = -b

        ans.a..(str(a // b))

        a %= b
        __ a __ 0:
            r.. ''.join(ans)

        ans.a..('.')
        D = {a: l..(ans)}  # the index of first occurrence of `a`
        while a:
            a *= 10
            ans.a..(str(a // b))
            a %= b

            __ a __ D:
                ans.insert(D[a], '(')
                ans.a..(')')
                break

            D[a] = l..(ans)

        r.. ''.join(ans)
