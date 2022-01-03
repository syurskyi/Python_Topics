"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
__author__ = 'Danyang'


c_ Solution:
    ___ isPalindrome(self, x):
        """
        Algorithm: int, compare lsb and msb
        No extra space
        If you are thinking of converting the integer to string, note the restriction of using extra space.

        :param x: int
        :return: boolean
        """
        __ x < 0:
            r.. F..

        # find order of magnitude
        div = 1
        w.... x/div >= 10:
            div *= 10  # without touch x

        w.... x > 0:
            msb = x/div
            lsb = x%10

            __ msb != lsb:
                r.. F..

            # shrink
            x %= div
            x /= 10

            div /= 100

        r.. T..


__ __name__ __ "__main__":
    Solution().isPalindrome(2147483647)