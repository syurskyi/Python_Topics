c_ Solution:
    ___ longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        __ n.. s:
            r.. ''

        start = size = 0

        ___ i __ r..(l..(s)):
            _start, _size = check_palindrome(s, i, i)

            __ _size > size:
                size = _size
                start = _start

            _start, _size = check_palindrome(s, i, i + 1)

            __ _size > size:
                size = _size
                start = _start

        r.. s[start:start + size]

    ___ check_palindrome(self, s, left, right):
        n = l..(s)

        w.... left >= 0 a.. right < n a.. s[left] __ s[right]:
            left -= 1
            right += 1

        r.. left + 1, right - left - 1
