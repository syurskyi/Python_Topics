class Solution:
    ___ computeLastDigit(self, a, b
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        __ not a or not b:
            r_ 0
        __ a __ b:
            r_ 1

        ans = 1

        for num in range(a + 1, b + 1
            __ ans __ 0:
                r_ 0

            ans *= num % 10
            ans %= 10

        r_ ans
