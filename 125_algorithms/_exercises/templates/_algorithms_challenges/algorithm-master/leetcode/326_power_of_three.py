class Solution:
    ___ isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        __ not n:
            return False

        for i in (81, 27, 9, 3):
            while n % i == 0:
                n //= i

        return n == 1
