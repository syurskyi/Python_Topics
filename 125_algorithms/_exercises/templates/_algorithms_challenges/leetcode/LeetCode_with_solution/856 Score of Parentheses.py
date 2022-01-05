#!/usr/bin/python3
"""
Given a balanced parentheses string S, compute the score of the string based on
the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""


c_ Solution:
    ___ scoreOfParentheses  S: s..) __ i..:
        """
        stk

        Every position in the string has a depth - some number of matching
        parentheses surrounding it
        """
        stk    # list
        ret = 0
        ___ s __ S:
            __ s __ "(":
                stk.a..(0)
            ____:
                cur = stk.pop()
                score = m..(2 * cur, 1)
                __ stk:
                    stk[-1] += score
                ____:
                    ret += score

        r.. ret

    ___ scoreOfParentheses_error  S: s..) __ i..:
        """
        stk
        """
        ret = 0
        cur_stk    # list
        ___ s __ S:
            __ s __ "(":
                cur_stk.a..(0)
                stk.a..(s)
            ____:
                stk.pop()
                __ cur_stk[-1] __ 0:
                    cur_stk[-1] = 1
                ____:
                    cur_stk[-1] *= 2
            __ n.. stk:
                ret += cur
                cur = 0

        r.. ret


__ _______ __ _______
    ... Solution().scoreOfParentheses("(())") __ 2
    ... Solution().scoreOfParentheses("(()(()))") __ 6
