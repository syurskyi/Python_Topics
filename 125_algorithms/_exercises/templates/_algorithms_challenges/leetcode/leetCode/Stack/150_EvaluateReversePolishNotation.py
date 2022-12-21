#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ evalRPN  tokens
        value_stack   # list
        ___ token __ tokens:
            __ token __ "+-*/":
                operand_2 = value_stack.pop()
                operand_1 = value_stack.pop()
                negative = 1
                __ operand_1 * operand_2 < 0:
                    negative = -1

                __ token __ "+":
                    result = operand_1 + operand_2
                ____ token __ "-":
                    result = operand_1 - operand_2
                ____ token __ "*":
                    result = operand_1 * operand_2
                ____
                    # Leetcode think 12/-7 = -1, 12/-13 = 0
                    result = abs(operand_1) / abs(operand_2) * negative

                value_stack.append(result)
            ____
                value_stack.append(int(token))
        r_ value_stack[-1]

"""
["18"]
["12", "-7", "/"]
["2", "1", "+", "3", "*"]
["4", "13", "5", "/", "+"]
"""
