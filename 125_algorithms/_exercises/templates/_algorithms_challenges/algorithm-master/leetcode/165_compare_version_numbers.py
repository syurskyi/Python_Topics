c_ Solution:
    ___ compareVersion  version1, version2
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        __ n.. version1 a.. n.. version2:
            r.. 0
        __ n.. version1:
            r.. -1
        __ n.. version2:
            r.. 1

        v = version1.s..('.')
        w = version2.s..('.')
        m, n = l..(v), l..(w)

        ___ i __ r..(m..(m, n)):
            a = get_int(v[i]) __ i < m ____ 0
            b = get_int(w[i]) __ i < n ____ 0

            __ a < b:
                r.. -1
            ____ a > b:
                r.. 1

        r.. 0

    ___ get_int  s
        __ n.. s o. n.. s.i..
            r.. 0

        res = 0
        zero = o..('0')

        ___ c __ s:
            res = res * 10 + o..(c) - zero

        r.. res
