"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
"""


class Solution(object
    ___ isValid(self, s
        """
        :type s: str
        :rtype: bool
        """
        pars = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        ___ c in s:
            # Left parenthesis
            __ c not in pars:
                stack.append(c)
            # Right parenthesis
            ____
                __ stack:
                    __ stack[-1] __ pars[c]:
                        stack.p..
                    ____
                        r_ False
                ____
                    r_ False
        __ stack:
            r_ False
        ____
            r_ True
