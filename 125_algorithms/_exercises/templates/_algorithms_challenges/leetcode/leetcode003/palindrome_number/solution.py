class Solution:
    # @return a boolean
    ___ isPalindrome(self, x):
        __ x < 0:
            return False
        num_digit = 0
        y = x
        while y != 0:
            y /= 10
            num_digit += 1
        __ num_digit <= 1:
            return True
        # Reverse the right half
        i = 0
        t = 0
        while i < num_digit / 2:
            t = t * 10 + x % 10
            x /= 10
            i += 1
        # Remove the middle digit if num_digit is odd
        __ num_digit % 2 == 1:
            x /= 10
        # Compare t and x
        __ t == x:
            return True
        else:
            return False
