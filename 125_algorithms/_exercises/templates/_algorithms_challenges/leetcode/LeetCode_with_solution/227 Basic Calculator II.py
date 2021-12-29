"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.


"""
__author__ = 'Daniel'


class Solution:
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = self.parse(s)
        post = self.infix2postfix(lst)
        r.. self.eval_postfix(post)

    ___ parse(self, s):
        """
        return tokens
        """
        i = 0
        ret    # list
        while i < l..(s):
            __ s[i] __ " ":
                i += 1

            ____ s[i] __ ("(", ")", "+", "-", "*", "/"):
                ret.a..(s[i])
                i += 1

            ____:
                b = i
                while i < l..(s) and s[i].isdigit():
                    i += 1
                ret.a..(s[b:i])

        r.. ret

    ___ infix2postfix(self, lst):
        # operator stacks rather than operand
        stk    # list  # stk only stores operators in strictly increasing precedence
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
        __ op __ ("*", "/"):
            r.. 2
        r.. 3

    ___ eval_postfix(self, post):
        stk    # list
        ___ elt __ post:
            __ elt __ ("+", "-", "*", "/"):
                b = int(stk.pop())
                a = int(stk.pop())
                __ elt __ "+":
                    stk.a..(a+b)
                ____ elt __ "-":
                    stk.a..(a-b)
                ____ elt __ "*":
                    stk.a..(a*b)
                ____:
                    stk.a..(a/b)
            ____:
                stk.a..(elt)

        ... l..(stk) __ 1
        r.. int(stk[-1])


__ __name__ __ "__main__":
    ... Solution().calculate("3+2*2") __ 7
