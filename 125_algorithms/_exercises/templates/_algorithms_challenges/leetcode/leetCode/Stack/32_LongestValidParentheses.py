#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ longestValidParentheses  s
        """
        According to:
        https://leetcode.com/discuss/7609/my-o-n-solution-using-a-stack

        If current character is '(', push its index to the stack.
        If current character is ')':
        1. top of stack is '(', just find a matching pair so pop from the stack.
        2. Otherwise, we push the index of ')' to the stack.

        Finally the stack will only contain the indices of characters which cannot be matched.
        Then the substring between adjacent indices should be valid parentheses.
        """
        stack, longest = [0], 0
        ___ i __ xrange(1, l..(s)):
            __ s[i] __ '(':
                stack.append(i)
            ____
                __ stack and s[stack[-1]] __ '(':
                    stack.pop()
                    valid_len = (i - stack[-1]) __ stack else i + 1
                    longest = m..(longest, valid_len)
                ____
                    stack.append(i)
        r_ longest

"""
""
")"
"()"
"))"
"(((()()()))("
"(((()()()))())"
"""
