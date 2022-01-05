#!/usr/bin/python3
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


c_ Solution:
    ___ calculate  s: s..) __ i..:
        """
        No brackets. Look at previous operand and operator, when finishing
        scanning current operand.
        """
        operand = 0
        stk    # list
        prev_op = "+"
        ___ i, c __ e..(s):
            __ c.isdigit
                operand = operand * 10 + i..(c)

            #  i == len(s) - 1
            delimited = c __ ("+", "-", "*", "/") o. i __ l..(s) - 1
            __ delimited:
                __ prev_op __ "+":
                    cur = operand
                ____ prev_op __ "-":
                    cur = -operand
                ____ prev_op __ "*":
                    cur = stk.pop() * operand
                ____:
                    ... prev_op __ "/"
                    # instead of op1 // op2 due to negative handling, -3 // 2 == -2
                    cur = i..(stk.pop() / operand)

                stk.a..(cur)
                prev_op = c
                operand = 0

        r.. s..(stk)

    ___ calculate_error  s: s..) __ i..:
        """
        cannot use dictionary, since it is eager evaluation
        """
        operand = 0
        stk    # list
        prev_op = "+"
        ___ i, c __ e..(s):
            __ c.isdigit
                operand = operand * 10 + i..(c)

            #  i == len(s) - 1
            delimited = c __ ("+", "-", "*", "/") o. i __ l..(s) - 1
            __ delimited:
                cur = {
                    "+": operand,
                    "-": -operand,
                    "*": stk.pop() * operand,
                    "/": i..(stk.pop() / operand),  # instead of op1 // op2 due to negative handling, -3 // 2 == -2
                }[prev_op]
                stk.a..(cur)

                prev_op = c
                operand = 0

        r.. s..(stk)


__ _______ __ _______
    ... Solution().calculate("3+2*2") __ 7
