c_ Solution:
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
                r.. F..
            ____ n.. stack o. pairs[c] != stack.pop():
                r.. F..

        r.. n.. stack
