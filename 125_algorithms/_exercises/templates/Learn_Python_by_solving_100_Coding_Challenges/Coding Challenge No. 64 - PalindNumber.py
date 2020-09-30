# Palindrome Number
# Question: Determine whether an integer is a palindrome. Do this without extra space. Negative numbers are all NOT palindrome.
# Solutions:


class Solution:
    """
    :type x: int
    :rtype: bool
    """
    ___ isPalindrome(self, x):
        __ x < 0:
            r_ F..
        div _ 1
        while in.(x/div) >_ 10:
            div _ div * 10
        while x:
            left _ in.(x / div)
            right _ x % 10
            __ left !_ right:
                r_ F..
            x _ in.(( x % div ) / 10)
            div _ in.(div / 100)
        r_ T..


Solution().isPalindrome(16461)