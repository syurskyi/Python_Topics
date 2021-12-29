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
        return self.eval_postfix(post)

    ___ parse(self, s):
        """
        return tokens
        """
        i = 0
        ret = []
        while i < len(s):
            __ s[i] == " ":
                i += 1

            elif s[i] in ("(", ")", "+", "-", "*", "/"):
                ret.append(s[i])
                i += 1

            else:
                b = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                ret.append(s[b:i])

        return ret

    ___ infix2postfix(self, lst):
        # operator stacks rather than operand
        stk = []  # stk only stores operators in strictly increasing precedence
        ret = []
        for elt in lst:
            __ elt.isdigit():
                ret.append(elt)
            elif elt == "(":
                stk.append(elt)
            elif elt == ")":
                while stk[-1] != "(":
                    ret.append(stk.pop())
                stk.pop()
            else:  # generalized to include * and /
                while stk and self.precendece(elt) <= self.precendece(stk[-1]):
                    ret.append(stk.pop())

                stk.append(elt)

        while stk:
            ret.append(stk.pop())

        return ret

    ___ precendece(self, op):
        __ op in ("(", ")"):
            return 0
        __ op in ("+", "-"):
            return 1
        __ op in ("*", "/"):
            return 2
        return 3

    ___ eval_postfix(self, post):
        stk = []
        for elt in post:
            __ elt in ("+", "-", "*", "/"):
                b = int(stk.pop())
                a = int(stk.pop())
                __ elt == "+":
                    stk.append(a+b)
                elif elt == "-":
                    stk.append(a-b)
                elif elt == "*":
                    stk.append(a*b)
                else:
                    stk.append(a/b)
            else:
                stk.append(elt)

        assert len(stk) == 1
        return int(stk[-1])


__ __name__ == "__main__":
    assert Solution().calculate("3+2*2") == 7
