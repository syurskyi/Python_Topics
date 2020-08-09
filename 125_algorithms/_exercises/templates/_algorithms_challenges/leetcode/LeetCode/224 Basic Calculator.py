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
    ___ calculate(self, s
        """
        * infix to postfix
        * eval postfix
        :type s: str
        :rtype: int
        """
        lst = self.to_list(s)
        postfix = self.infix2postfix(lst)
        r_ self.eval_postfix(postfix)

    ___ to_list(self, s
        i = 0
        ret = []
        w___ i < le.(s
            __ s[i] __ " ":
                i += 1

            ____ s[i] in ("(", ")", "+", "-"
                ret.append(s[i])
                i += 1

            ____
                b = i
                w___ i < le.(s) and s[i].isdigit(
                    i += 1
                ret.append(s[b:i])

        r_ ret

    ___ infix2postfix(self, lst
        stk = []  # store operators in strictly increasing precedence
        ret = []
        ___ elt in lst:
            __ elt.isdigit(
                ret.append(elt)
            ____ elt __ "(":
                stk.append(elt)
            ____ elt __ ")":
                w___ stk[-1] != "(":
                    ret.append(stk.pop())
                stk.pop()
            ____  # generalized to include * and /
                w___ stk and self.precendece(elt) <= self.precendece(stk[-1]
                    ret.append(stk.pop())

                stk.append(elt)

        w___ stk:
            ret.append(stk.pop())

        r_ ret

    ___ precendece(self, op
        __ op in ("(", ")"
            r_ 0
        __ op in ("+", "-"
            r_ 1

    ___ eval_postfix(self, post
        stk = []
        ___ elt in post:
            __ elt in ("+", "-"
                b = int(stk.pop())
                a = int(stk.pop())
                __ elt __ "+":
                    stk.append(a+b)
                ____
                    stk.append(a-b)
            ____
                stk.append(elt)

        assert le.(stk) __ 1
        r_ int(stk[-1])


__ __name__ __ "__main__":
    assert Solution().calculate(" 2-1 + 2 ") __ 3
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") __ 23