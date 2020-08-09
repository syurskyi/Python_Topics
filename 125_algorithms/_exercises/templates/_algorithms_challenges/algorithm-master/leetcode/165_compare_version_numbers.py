class Solution:
    ___ compareVersion(self, version1, version2
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        __ not version1 and not version2:
            r_ 0
        __ not version1:
            r_ -1
        __ not version2:
            r_ 1

        v = version1.split('.')
        w = version2.split('.')
        m, n = le.(v), le.(w)

        ___ i in range(max(m, n)):
            a = self.get_int(v[i]) __ i < m else 0
            b = self.get_int(w[i]) __ i < n else 0

            __ a < b:
                r_ -1
            ____ a > b:
                r_ 1

        r_ 0

    ___ get_int(self, s
        __ not s or not s.isdigit(
            r_ 0

        res = 0
        zero = ord('0')

        ___ c in s:
            res = res * 10 + ord(c) - zero

        r_ res
