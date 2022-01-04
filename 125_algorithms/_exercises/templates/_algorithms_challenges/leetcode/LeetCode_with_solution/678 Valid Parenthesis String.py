#!/usr/bin/python3
"""
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity
of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""


c_ Solution:
    ___ checkValidString(self, s: s..) __ bool:
        """
        Brute force: dfs branching on "*".

        Better Solution:
        keep two stack: stak of "(" and stack of "*"
        """
        stk_left    # list
        stk_star    # list
        ___ i, c __ e..(s):
            __ c __ "(":
                stk_left.a..(i)
            ____ c __ "*":
                stk_star.a..(i)
            ____:
                __ stk_left:
                    stk_left.pop()
                ____ stk_star:
                    stk_star.pop()
                ____:
                    r.. F..

        w.... stk_left a.. stk_star a.. stk_star[-1] > stk_left[-1]:
            stk_star.pop()
            stk_left.pop()

        r.. n.. stk_left


__ _______ __ _______
    ... Solution().checkValidString("(*))") __ T..
    ... Solution().checkValidString("*(") __ F..
    ... Solution().checkValidString("(*)") __ T..
