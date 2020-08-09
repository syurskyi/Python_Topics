class Solution:
    ___ isValid(self, s
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        ___ c in s:
            __ c in '([{':
                stack.append(c)
            ____ c not in ')]}':
                r_ False
            ____ not stack or pairs[c] != stack.pop(
                r_ False

        r_ not stack
