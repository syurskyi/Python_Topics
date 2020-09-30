# Palindrome Number
# Question: Determine whether an integer is a palindrome. Do this without extra space. Negative numbers are all NOT palindrome.
# Solutions:


class Solution:
    """
    :type x: int
    :rtype: bool
    """
    ___ isPalindrome(self, x):
        if x < 0:
            r_ False
        div = 1
        while int(x/div) >= 10:
            div = div * 10
        while x:
            left = int(x / div)
            right = x % 10
            if left != right:
                r_ False
            x = int(( x % div ) / 10)
            div = int(div / 100)
        r_ True


Solution().isPalindrome(16461)