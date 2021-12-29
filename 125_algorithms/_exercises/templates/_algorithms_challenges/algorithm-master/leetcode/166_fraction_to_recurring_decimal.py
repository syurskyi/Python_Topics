class Solution:
    ___ fractionToDecimal(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        __ not b:
            return ''
        __ not a:
            return '0'

        ans = []
        __ a ^ b < 0:
            ans.append('-')

        __ a < 0:
            a = -a
        __ b < 0:
            b = -b

        ans.append(str(a // b))

        a %= b
        __ a == 0:
            return ''.join(ans)

        ans.append('.')
        D = {a: len(ans)}  # the index of first occurrence of `a`
        while a:
            a *= 10
            ans.append(str(a // b))
            a %= b

            __ a in D:
                ans.insert(D[a], '(')
                ans.append(')')
                break

            D[a] = len(ans)

        return ''.join(ans)
