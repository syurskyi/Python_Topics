class Solution:
    ___ rotatedDigits(self, N
        """
        :type N: int
        :rtype: int
        """
        ans = 0

        ___ i in range(1, N + 1
            __ self.is_good(i
                ans += 1

        r_ ans

    ___ is_good(self, N
        res = False

        w___ N > 0:
            D = N % 10
            __ D in (3, 4, 7
                r_ False
            __ D in (2, 5, 6, 9
                res = True
            N = N // 10

        r_ res
