class Solution:
    ___ compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        __ not version1 and not version2:
            return 0
        __ not version1:
            return -1
        __ not version2:
            return 1

        v = version1.split('.')
        w = version2.split('.')
        m, n = len(v), len(w)

        for i in range(max(m, n)):
            a = self.get_int(v[i]) __ i < m else 0
            b = self.get_int(w[i]) __ i < n else 0

            __ a < b:
                return -1
            elif a > b:
                return 1

        return 0

    ___ get_int(self, s):
        __ not s or not s.isdigit():
            return 0

        res = 0
        zero = ord('0')

        for c in s:
            res = res * 10 + ord(c) - zero

        return res
