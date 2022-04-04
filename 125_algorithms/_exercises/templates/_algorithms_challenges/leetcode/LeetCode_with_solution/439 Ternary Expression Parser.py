#!/usr/bin/python3
"""
Premium question
"""


c_ Solution:
    ___ parseTernary  expression: s..) __ s..:
        """
        stk from right to left parsing, including the operand and operator
        """
        stk    # list
        ___ c __ r..(expression
            __ stk a.. stk[-1] __ "?":
                stk.p.. )  # ?
                first = stk.p.. )
                stk.p.. )  # :
                second = stk.p.. )
                __ c __ "T":
                    stk.a..(first)
                ____
                    stk.a..(second)
            ____
                stk.a..(c)

        r.. stk[0]

    ___ parseTernary_complex  expression: s..) __ s..:
        """
        tokenize + recursive (dfs)?

        stk from right to left, only include the operand

        can handle multiple digit (not required)
        """
        n = l..(expression)
        stk    # list
        i = n - 1
        w.... i >_ 0:
            j = i
            w.... j >_ 0 a.. expression[j] n.. __ (":", "?"
                j -= 1

            __ j < i:
                stk.a..(expression[j+1:i+1])

            __ expression[j] __ ":":
                i = j - 1
            ____  # "?"
                i = j - 1
                __ expression[i] __ "T":
                    a = stk.p.. )
                    stk.p.. )
                    stk.a..(a)
                    i -= 1
                ____
                    stk.p.. )
                    i -= 1

        r.. stk[0]



__ _______ __ _______
    ... Solution().parseTernary("F?1:T?4:5") __ "4"
    ... Solution().parseTernary("T?T?F:5:3") __ "F"
