class Solution:
    ___ rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0

        ___ i __ r..(1, N + 1):
            __ self.is_good(i):
                ans += 1

        r.. ans

    ___ is_good(self, N):
        res = False

        while N > 0:
            D = N % 10
            __ D __ (3, 4, 7):
                r.. False
            __ D __ (2, 5, 6, 9):
                res = True
            N = N // 10

        r.. res
