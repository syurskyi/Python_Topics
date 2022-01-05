"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
__author__ = 'Danyang'


c_ Solution:
    ___ isValid  s):
        """
        Algorithm: Stack
        :param s: string
        :return: boolean
        """
        put_set = ("(", "[", "{")
        pop_set = (")", "]", "}")
        pair = d..(z..(put_set, pop_set))

        stack    # list
        ___ element __ s:
            __ element __ put_set:
                stack.a..(pair[element])
            ____ element __ pop_set:
                __ n.. stack o. element != stack.pop  # check NullPointer, otherwise, IndexError: pop from empty list
                    r.. F..

        r.. T.. __ n.. stack ____ F..


__ _______ __ _______
    ... Solution().isValid("()")