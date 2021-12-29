class Solution:
    # @return a boolean
    ___ isPalindrome(self, x):
        __ x < 0:
            r.. False
        num_digit = 0
        y = x
        w.... y != 0:
            y /= 10
            num_digit += 1
        __ num_digit <= 1:
            r.. True
        # Reverse the right half
        i = 0
        t = 0
        w.... i < num_digit / 2:
            t = t * 10 + x % 10
            x /= 10
            i += 1
        # Remove the middle digit if num_digit is odd
        __ num_digit % 2 __ 1:
            x /= 10
        # Compare t and x
        __ t __ x:
            r.. True
        ____:
            r.. False
