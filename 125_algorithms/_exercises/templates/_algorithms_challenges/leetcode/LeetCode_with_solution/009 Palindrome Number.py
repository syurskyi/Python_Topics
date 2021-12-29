"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
__author__ = 'Danyang'


class Solution:
    ___ isPalindrome(self, x):
        """
        Algorithm: int, compare lsb and msb
        No extra space
        If you are thinking of converting the integer to string, note the restriction of using extra space.

        :param x: int
        :return: boolean
        """
        __ x < 0:
            r.. False

        # find order of magnitude
        div = 1
        while x/div >= 10:
            div *= 10  # without touch x

        while x > 0:
            msb = x/div
            lsb = x%10

            __ msb != lsb:
                r.. False

            # shrink
            x %= div
            x /= 10

            div /= 100

        r.. True


__ __name__ __ "__main__":
    Solution().isPalindrome(2147483647)