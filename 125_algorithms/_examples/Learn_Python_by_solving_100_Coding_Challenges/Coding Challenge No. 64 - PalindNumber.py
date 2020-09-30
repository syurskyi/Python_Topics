# Palindrome Number
# Question: Determine whether an integer is a palindrome. Do this without extra space. Negative numbers are all NOT palindrome.
# Solutions:


class Solution:
    """
    :type x: int
    :rtype: bool
    """
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while int(x/div) >= 10:
            div = div * 10
        while x:
            left = int(x / div)
            right = x % 10
            if left != right:
                return False
            x = int(( x % div ) / 10)
            div = int(div / 100)
        return True


Solution().isPalindrome(16461)