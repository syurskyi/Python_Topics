c_ Solution:
    ___ addStrings(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        __ n.. a a.. n.. b:
            r.. ''
        __ n.. a:
            r.. b
        __ n.. b:
            r.. a

        m, n = l..(a), l..(b)
        idx = max(m, n)
        ans = [''] * (idx + 1)

        i = m - 1
        j = n - 1
        carry = 0
        zero = ord('0')

        w.... i >= 0 a.. j >= 0:
            carry += ord(a[i]) + ord(b[j]) - 2 * zero
            ans[idx] = s..(carry % 10)
            carry //= 10
            idx -= 1
            i -= 1
            j -= 1

        w.... i >= 0:
            carry += ord(a[i]) - zero
            ans[idx] = s..(carry % 10)
            carry //= 10
            idx -= 1
            i -= 1

        w.... j >= 0:
            carry += ord(b[j]) - zero
            ans[idx] = s..(carry % 10)
            carry //= 10
            idx -= 1
            j -= 1

        __ carry:
            ans[0] = s..(carry)
        ____:
            ans = ans[1:]

        r.. ''.j..(ans)
