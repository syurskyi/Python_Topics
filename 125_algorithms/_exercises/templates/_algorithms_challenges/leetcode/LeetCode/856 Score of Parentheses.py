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


class Solution:
    ___ scoreOfParentheses(self, S: str) -> int:
        """
        stk

        Every position in the string has a depth - some number of matching
        parentheses surrounding it
        """
        stk = []
        ret = 0
        ___ s in S:
            __ s __ "(":
                stk.append(0)
            ____
                cur = stk.pop()
                score = max(2 * cur, 1)
                __ stk:
                    stk[-1] += score
                ____
                    ret += score

        r_ ret

    ___ scoreOfParentheses_error(self, S: str) -> int:
        """
        stk
        """
        ret = 0
        cur_stk = []
        ___ s in S:
            __ s __ "(":
                cur_stk.append(0)
                stk.append(s)
            ____
                stk.pop()
                __ cur_stk[-1] __ 0:
                    cur_stk[-1] = 1
                ____
                    cur_stk[-1] *= 2
            __ not stk:
                ret += cur
                cur = 0

        r_ ret


__ __name__ __ "__main__":
    assert Solution().scoreOfParentheses("(())") __ 2
    assert Solution().scoreOfParentheses("(()(()))") __ 6
