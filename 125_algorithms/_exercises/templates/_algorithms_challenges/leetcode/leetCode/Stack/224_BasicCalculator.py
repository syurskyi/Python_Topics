#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# According to:
# https://leetcode.com/discuss/39553/iterative-java-solution-with-stack


c.. Solution o..
    """
    1. Start from + sign and scan s from left to right;
    2. if c == digit: This number = Last digit * 10 + This digit;
    3. if c == '+': Add num to result before this sign;
        This sign = Last context sign * 1; clear num;
    4. if c == '-': Add num to result before this sign;
        This sign = Last context sign * -1; clear num;
    5. if c == '(': Push this context sign to stack;
    6. if c == ')': Pop this context and we come back to last context;
    7. Add the last num. This is because we only add number after '+' / '-'.
    """
    ___ calculate  s
        # s = "".join(s.split(" "))     # Erase the redundant space
        sign = 1
        sign_stack = [1]
        num, result = 0, 0
        ___ ch __ s:
            __ ch __ " ":
                pass
            ____ ch __ "(":
                sign_stack.a.. sign)
            ____ ch __ "+-":
                result += num * sign
                sign = sign_stack[-1] * (1 __ ch __ "+" else -1)
                num = 0
            ____ ch __ ")":
                sign_stack.pop()
            ____
                num = num * 10 + int(ch)
        result += num * sign
        r_ result

"""
" 1234 "
"1 + 1"
" 2-1 + 2 "
" 2  - (1+2-(1+2))"
"(1+(4+5+2)-3)+(6+8)"
"""
