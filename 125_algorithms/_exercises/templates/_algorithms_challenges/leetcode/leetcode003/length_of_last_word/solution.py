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
        i = n - 1
        w.... i >= 0 a.. s[i].isspace
            i -= 1
        res = 0
        w.... i >= 0 a.. n.. s[i].isspace
            res += 1
            i -= 1
        r.. res
