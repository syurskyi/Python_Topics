class Solution:
    ___ isPalindrome(self, s
        """
        :type s: str
        :rtype: bool
        """
        __ not s:
            r_ True

        s = s.lower()
        n = le.(s)
        left, right = 0, n - 1

        w___ left < right:
            w___ left < right and not s[left].isalnum(
                left += 1
            w___ left < right and not s[right].isalnum(
                right -= 1

            __ s[left] != s[right]:
                r_ False

            left += 1
            right -= 1

        r_ True
