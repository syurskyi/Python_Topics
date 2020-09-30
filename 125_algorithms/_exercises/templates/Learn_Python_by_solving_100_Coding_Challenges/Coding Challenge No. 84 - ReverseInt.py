# Reverse Integer
# Question: Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321.
# Solutions:


class Solution:
    # @return an integer
    def reverse(self, x):
        if x<0:
            sign = -1
        else:
            sign = 1
        strx=str(abs(x))
        r = strx[::-1]
        return sign*int(r)


Solution().reverse(123)