#!/usr/bin/python3
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
____ typing _______ List


c_ Solution:
    ___ calculate(self, s: s..) __ i..:
        """
        1. treat +/- as unary operator
        2. maintain stk of operands to sum
        3. handle bracket recursively
        """
        ret, _ = eval(s + "\0", 0, [])
        r.. ret

    ___ eval(self, s: s.., start: i.., stk: List[i..]) __ i..:
        prev_op = "+"
        operand = 0
        i = start
        w.... i < l..(s):  #  not using for-loop, since the cursor needs to advance in recursion
            __ s[i] __ " ":
                p..
            ____ s[i].isdigit
                operand = operand * 10 + i..(s[i])
            ____ s[i] __ ("+", "-", ")", "\0"):  # delimited
                __ prev_op __ "+":
                    stk.a..(operand)
                ____ prev_op __ "-":
                    stk.a..(-operand)
        
                __ s[i] __ ("+", "-"):
                    operand = 0
                    prev_op = s[i]
                ____ s[i] __ (")", "\0"):
                    r.. s..(stk), i
            ____ s[i] __ "(":
                # avoid setting operand to 0
                operand, i = eval(s, i + 1, [])
            ____:
                raise

            i += 1


__ __name__ __ "__main__":
    ... Solution().calculate("(1+(4+5+2)-3)+(6+8)") __ 23
