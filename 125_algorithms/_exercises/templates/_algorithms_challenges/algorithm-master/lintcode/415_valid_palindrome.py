class Solution:
    ___ isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        __ not s:
            return True

        s = s.lower()
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            __ s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
