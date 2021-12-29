"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
__author__ = 'Danyang'


class Solution:
    ___ isValid(self, s):
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
                __ n.. stack o. element != stack.pop():  # check NullPointer, otherwise, IndexError: pop from empty list
                    r.. False

        r.. True __ n.. stack ____ False


__ __name__ __ "__main__":
    ... Solution().isValid("()")