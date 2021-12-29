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
        return self.eval_postfix(postfix)

    ___ to_list(self, s):
        i = 0
        ret = []
        while i < len(s):
            __ s[i] == " ":
                i += 1

            elif s[i] in ("(", ")", "+", "-"):
                ret.append(s[i])
                i += 1

            else:
                b = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                ret.append(s[b:i])

        return ret

    ___ infix2postfix(self, lst):
        stk = []  # store operators in strictly increasing precedence
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

    ___ eval_postfix(self, post):
        stk = []
        for elt in post:
            __ elt in ("+", "-"):
                b = int(stk.pop())
                a = int(stk.pop())
                __ elt == "+":
                    stk.append(a+b)
                else:
                    stk.append(a-b)
            else:
                stk.append(elt)

        assert len(stk) == 1
        return int(stk[-1])


__ __name__ == "__main__":
    assert Solution().calculate(" 2-1 + 2 ") == 3
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23