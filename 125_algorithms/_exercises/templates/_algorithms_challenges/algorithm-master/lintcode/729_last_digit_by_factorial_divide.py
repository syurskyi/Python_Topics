class Solution:
    ___ computeLastDigit(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        __ not a or not b:
            return 0
        __ a == b:
            return 1

        ans = 1

        for num in range(a + 1, b + 1):
            __ ans == 0:
                return 0

            ans *= num % 10
            ans %= 10

        return ans
