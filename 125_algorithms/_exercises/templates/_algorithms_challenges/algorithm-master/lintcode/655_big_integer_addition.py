c_ Solution:
    ___ addStrings  a, b
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

        m, n l..(a), l..(b)
        idx m..(m, n)
        ans [''] * (idx + 1)

        i m - 1
        j n - 1
        carry 0
        zero o..('0')

        w.... i >_ 0 a.. j >_ 0:
            carry += o..(a[i]) + o..(b[j]) - 2 * zero
            ans[idx] s..(carry % 10)
            carry //= 10
            idx -_ 1
            i -_ 1
            j -_ 1

        w.... i >_ 0:
            carry += o..(a[i]) - zero
            ans[idx] s..(carry % 10)
            carry //= 10
            idx -_ 1
            i -_ 1

        w.... j >_ 0:
            carry += o..(b[j]) - zero
            ans[idx] s..(carry % 10)
            carry //= 10
            idx -_ 1
            j -_ 1

        __ carry:
            ans[0] s..(carry)
        ____
            ans ans[1:]

        r.. ''.j..(ans)
