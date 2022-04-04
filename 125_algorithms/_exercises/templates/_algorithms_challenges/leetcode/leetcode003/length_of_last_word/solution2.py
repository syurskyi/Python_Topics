"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

For example, Given s = "Hello World",
return 5.
"""

c_ Solution(o..
    ___ lengthOfLastWord  s
        """
        :type s: str
        :rtype: int
        """
        n = l..(s)
        p = n - 1
        right = -1
        w.... p >_ 0:
            __ right __ -1 a.. s[p] != ' ':
                right = p
            ____ right >_ 0 a.. s[p] __ ' ':
                r.. right - p
            p -= 1
        __ right >_ 0:
            r.. right + 1
        ____
            r.. 0
