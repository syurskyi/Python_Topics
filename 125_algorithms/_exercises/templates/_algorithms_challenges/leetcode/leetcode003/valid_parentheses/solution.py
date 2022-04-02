"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
"""


c_ Solution(o..
    ___ isValid  s
        """
        :type s: str
        :rtype: bool
        """
        pars = {
            ')': '(',
            ' ': ' ',
            '}': '{',
        }
        stack    # list
        ___ c __ s:
            # Left parenthesis
            __ c n.. __ pars:
                stack.a..(c)
            # Right parenthesis
            ____:
                __ stack:
                    __ stack[-1] __ pars[c]:
                        stack.pop()
                    ____:
                        r.. F..
                ____:
                    r.. F..
        __ stack:
            r.. F..
        ____:
            r.. T..
