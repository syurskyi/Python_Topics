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
    ___ calculate(self, s
        """
        :type s: str
        :rtype: int
        """
        lst = self.parse(s)
        post = self.infix2postfix(lst)
        r_ self.eval_postfix(post)

    ___ parse(self, s
        """
        return tokens
        """
        i = 0
        ret = []
        w___ i < le.(s
            __ s[i] __ " ":
                i += 1

            ____ s[i] in ("(", ")", "+", "-", "*", "/"
                ret.append(s[i])
                i += 1

            ____
                b = i
                w___ i < le.(s) and s[i].isdigit(
                    i += 1
                ret.append(s[b:i])

        r_ ret

    ___ infix2postfix(self, lst
        # operator stacks rather than operand
        stk = []  # stk only stores operators in strictly increasing precedence
        ret = []
        for elt in lst:
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
        __ op in ("*", "/"
            r_ 2
        r_ 3

    ___ eval_postfix(self, post
        stk = []
        for elt in post:
            __ elt in ("+", "-", "*", "/"
                b = int(stk.pop())
                a = int(stk.pop())
                __ elt __ "+":
                    stk.append(a+b)
                ____ elt __ "-":
                    stk.append(a-b)
                ____ elt __ "*":
                    stk.append(a*b)
                ____
                    stk.append(a/b)
            ____
                stk.append(elt)

        assert le.(stk) __ 1
        r_ int(stk[-1])


__ __name__ __ "__main__":
    assert Solution().calculate("3+2*2") __ 7
