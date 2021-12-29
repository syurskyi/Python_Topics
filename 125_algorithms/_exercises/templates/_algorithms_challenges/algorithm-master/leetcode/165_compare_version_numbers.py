class Solution:
    ___ compareVersion(self, version1, version2):
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

        ___ i __ r..(max(m, n)):
            a = self.get_int(v[i]) __ i < m ____ 0
            b = self.get_int(w[i]) __ i < n ____ 0

            __ a < b:
                r.. -1
            ____ a > b:
                r.. 1

        r.. 0

    ___ get_int(self, s):
        __ n.. s o. n.. s.isdigit():
            r.. 0

        res = 0
        zero = ord('0')

        ___ c __ s:
            res = res * 10 + ord(c) - zero

        r.. res
