class Solution:
    ___ longestPalindrome(self, s
        """
        :type s: str
        :rtype: str
        """
        __ not s:
            r_ ''

        start = size = 0

        for i in range(le.(s)):
            _start, _size = self.check_palindrome(s, i, i)

            __ _size > size:
                size = _size
                start = _start

            _start, _size = self.check_palindrome(s, i, i + 1)

            __ _size > size:
                size = _size
                start = _start

        r_ s[start:start + size]

    ___ check_palindrome(self, s, left, right
        n = le.(s)

        w___ left >= 0 and right < n and s[left] __ s[right]:
            left -= 1
            right += 1

        r_ left + 1, right - left - 1
