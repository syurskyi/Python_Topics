#!/usr/bin/python3
"""
Premium question
"""


class Solution:
    ___ parseTernary(self, expression: str) -> str:
        """
        stk from right to left parsing, including the operand and operator
        """
        stk =   # list
        ___ c __ reversed(expression
            __ stk and stk[-1] __ "?":
                stk.p..  # ?
                first = stk.p..
                stk.p..  # :
                second = stk.p..
                __ c __ "T":
                    stk.append(first)
                ____
                    stk.append(second)
            ____
                stk.append(c)

        r_ stk[0]

    ___ parseTernary_complex(self, expression: str) -> str:
        """
        tokenize + recursive (dfs)?

        stk from right to left, only include the operand

        can handle multiple digit (not required)
        """
        n = le.(expression)
        stk =   # list
        i = n - 1
        w___ i >= 0:
            j = i
            w___ j >= 0 and expression[j] not __ (":", "?"
                j -= 1

            __ j < i:
                stk.append(expression[j+1:i+1])

            __ expression[j] __ ":":
                i = j - 1
            ____  # "?"
                i = j - 1
                __ expression[i] __ "T":
                    a = stk.p..
                    stk.p..
                    stk.append(a)
                    i -= 1
                ____
                    stk.p..
                    i -= 1

        r_ stk[0]



__  -n __ "__main__":
    assert Solution().parseTernary("F?1:T?4:5") __ "4"
    assert Solution().parseTernary("T?T?F:5:3") __ "F"
