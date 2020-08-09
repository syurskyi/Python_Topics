class Solution:
    ___ addStrings(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        __ not a and not b:
            r_ ''
        __ not a:
            r_ b
        __ not b:
            r_ a

        m, n = le.(a), le.(b)
        idx = max(m, n)
        ans = [''] * (idx + 1)

        i = m - 1
        j = n - 1
        carry = 0
        zero = ord('0')

        w___ i >= 0 and j >= 0:
            carry += ord(a[i]) + ord(b[j]) - 2 * zero
            ans[idx] = str(carry % 10)
            carry //= 10
            idx -= 1
            i -= 1
            j -= 1

        w___ i >= 0:
            carry += ord(a[i]) - zero
            ans[idx] = str(carry % 10)
            carry //= 10
            idx -= 1
            i -= 1

        w___ j >= 0:
            carry += ord(b[j]) - zero
            ans[idx] = str(carry % 10)
            carry //= 10
            idx -= 1
            j -= 1

        __ carry:
            ans[0] = str(carry)
        ____
            ans = ans[1:]

        r_ ''.join(ans)
