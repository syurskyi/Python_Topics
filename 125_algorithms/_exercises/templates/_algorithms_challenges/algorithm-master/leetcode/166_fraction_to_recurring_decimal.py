class Solution:
    ___ fractionToDecimal(self, a, b
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        __ not b:
            r_ ''
        __ not a:
            r_ '0'

        ans = []
        __ a ^ b < 0:
            ans.append('-')

        __ a < 0:
            a = -a
        __ b < 0:
            b = -b

        ans.append(str(a // b))

        a %= b
        __ a __ 0:
            r_ ''.join(ans)

        ans.append('.')
        D = {a: le.(ans)}  # the index of first occurrence of `a`
        w___ a:
            a *= 10
            ans.append(str(a // b))
            a %= b

            __ a in D:
                ans.insert(D[a], '(')
                ans.append(')')
                break

            D[a] = le.(ans)

        r_ ''.join(ans)
