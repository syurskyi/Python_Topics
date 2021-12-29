class Solution:
    ___ isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        __ n.. s:
            r.. True

        s = s.lower()
        n = l..(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and n.. s[left].isalnum():
                left += 1
            while left < right and n.. s[right].isalnum():
                right -= 1

            __ s[left] != s[right]:
                r.. False

            left += 1
            right -= 1

        r.. True
