class Solution:
    ___ multiply(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        __ not a or not b or a __ '0' or b __ '0':
            r_ '0'

        m, n = le.(a), le.(b)
        tmp = [0] * (m + n)

        ___ i in range(m - 1, -1, -1
            carry = 0
            ___ j in range(n - 1, -1, -1
                carry += tmp[i + j + 1] + int(a[i]) * int(b[j])
                tmp[i + j + 1] = carry % 10
                carry //= 10
            tmp[i] = carry

        i = 0
        w___ tmp[i] __ 0:
            i += 1

        r_ ''.join([str(j) ___ j in tmp[i:]])
