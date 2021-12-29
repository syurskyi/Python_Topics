class Solution:
    ___ isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        __ not num:
            return False
        __ num == 1:
            return True

        for factor in (
            125, 27, 8,
            5, 3, 2,
        ):
            while num % factor == 0:
                num //= factor

            __ num == 1:
                return True

        return num == 1
