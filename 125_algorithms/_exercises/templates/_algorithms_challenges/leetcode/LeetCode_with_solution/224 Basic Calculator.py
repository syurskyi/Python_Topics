"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
and empty spaces.

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
"""
__author__ = 'Daniel'


class Solution:
    ___ calculate(self, s):
        """
        * infix to postfix
        * eval postfix
        :type s: str
        :rtype: int
        """
        lst = self.to_list(s)
        postfix = self.infix2postfix(lst)
        r.. self.eval_postfix(postfix)

    ___ to_list(self, s):
        i = 0
        ret    # list
        while i < l..(s):
            __ s[i] __ " ":
                i += 1

            ____ s[i] __ ("(", ")", "+", "-"):
                ret.a..(s[i])
                i += 1

            ____:
                b = i
                while i < l..(s) and s[i].isdigit():
                    i += 1
                ret.a..(s[b:i])

        r.. ret

    ___ infix2postfix(self, lst):
        stk    # list  # store operators in strictly increasing precedence
        ret    # list
        ___ elt __ lst:
            __ elt.isdigit():
                ret.a..(elt)
            ____ elt __ "(":
                stk.a..(elt)
            ____ elt __ ")":
                while stk[-1] != "(":
                    ret.a..(stk.pop())
                stk.pop()
            ____:  # generalized to include * and /
                while stk and self.precendece(elt) <= self.precendece(stk[-1]):
                    ret.a..(stk.pop())

                stk.a..(elt)

        while stk:
            ret.a..(stk.pop())

        r.. ret

    ___ precendece(self, op):
        __ op __ ("(", ")"):
            r.. 0
        __ op __ ("+", "-"):
            r.. 1

    ___ eval_postfix(self, post):
        stk    # list
        ___ elt __ post:
            __ elt __ ("+", "-"):
                b = int(stk.pop())
                a = int(stk.pop())
                __ elt __ "+":
                    stk.a..(a+b)
                ____:
                    stk.a..(a-b)
            ____:
                stk.a..(elt)

        ... l..(stk) __ 1
        r.. int(stk[-1])


__ __name__ __ "__main__":
    ... Solution().calculate(" 2-1 + 2 ") __ 3
    ... Solution().calculate("(1+(4+5+2)-3)+(6+8)") __ 23