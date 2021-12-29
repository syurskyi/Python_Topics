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

        w.... left < right:
            w.... left < right a.. n.. s[left].isalnum():
                left += 1
            w.... left < right a.. n.. s[right].isalnum():
                right -= 1

            __ s[left] != s[right]:
                r.. False

            left += 1
            right -= 1

        r.. True
