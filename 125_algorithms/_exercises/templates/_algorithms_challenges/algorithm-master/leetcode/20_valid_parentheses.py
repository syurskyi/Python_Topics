class Solution:
    ___ isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack    # list
        pairs = {')': '(', ']': '[', '}': '{'}

        ___ c __ s:
            __ c __ '([{':
                stack.a..(c)
            ____ c n.. __ ')]}':
                r.. False
            ____ n.. stack o. pairs[c] != stack.pop():
                r.. False

        r.. n.. stack
