c_ Solution:
    ___ multiply  a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        __ n.. a o. n.. b o. a __ '0' o. b __ '0':
            r.. '0'

        m, n = l..(a), l..(b)
        tmp = [0] * (m + n)

        ___ i __ r..(m - 1, -1, -1):
            carry = 0
            ___ j __ r..(n - 1, -1, -1):
                carry += tmp[i + j + 1] + i..(a[i]) * i..(b[j])
                tmp[i + j + 1] = carry % 10
                carry //= 10
            tmp[i] = carry

        i = 0
        w.... tmp[i] __ 0:
            i += 1

        r.. ''.j..([s..(j) ___ j __ tmp[i:]])
