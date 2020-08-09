"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

For example, Given s = "Hello World",
return 5.
"""

class Solution(object
    ___ lengthOfLastWord(self, s
        """
        :type s: str
        :rtype: int
        """
        n = le.(s)
        i = n - 1
        res = 0
        w___ i >= 0:
            __ s[i] != ' ':
                res += 1
            ____
                __ res != 0:
                    break
            i -= 1
        r_ res
