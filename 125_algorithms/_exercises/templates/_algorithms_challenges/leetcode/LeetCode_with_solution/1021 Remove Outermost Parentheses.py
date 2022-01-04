#!/usr/bin/python3
"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where
A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not
exist a way to split it into S = A+B, with A and B nonempty valid parentheses
strings.

Given a valid parentheses string S, consider its primitive decomposition:
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in
the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition
"(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" +
"()(())" = "()()()()(())".

Example 3:
Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:
S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""
____ c.. _______ d..


c_ Solution:
    ___ removeOuterParentheses(self, S: s..) __ s..:
        """
        Primitive parentheses will have equal number of opened and closed
        parentheses.

        Use count
        Exclude the first and last parathesis
        """
        ret    # list
        cnt = 0
        ___ e __ S:
            __ e __ "(":
                cnt += 1
                __ cnt > 1:
                    ret.a..(e)
            ____:
                cnt -= 1
                __ cnt > 0:
                    ret.a..(e)

        r.. "".j..(ret)


    ___ removeOuterParentheses_error(self, S: s..) __ s..:
        """
        stack + deque
        """
        ret    # list
        stk    # list
        cur_q = d..()
        ___ e __ S:
            __ e __ "(":
                stk.a..(e)
            ____:
                prev = stk.pop()
                __ stk:
                    cur_q.appendleft(prev)
                    cur_q.a..(e)
                ____:
                    ret.extend(cur_q)
                    cur_q = d..()

        r.. "".j..(ret)


__ _______ __ _______
    ... Solution().removeOuterParentheses("(()())(())(()(()))") __ "()()()()(())"
