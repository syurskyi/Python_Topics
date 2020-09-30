class Solution:
    ___ calculate(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ 0

        self.OP = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
        }

        s = self.to_rpn(s)

        __ not s:
            r_ 0

        r_ self.eval_rpn(s)

    ___ to_rpn(self, s
        stack, res =   # list, []

        ___ i __ range(le.(s)):
            char = s[i]

            __ i > 0 and s[i - 1].isdigit() and char.isdigit(
                res[-1] += char
            ____ char.isdigit(
                res.append(char)
            ____ char __ self.OP:
                w___ stack and stack[-1] __ self.OP:
                    res.append(stack.pop())
                stack.append(char)
            ____ char __ '(':
                stack.append(char)
            ____ char __ ')':
                w___ stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.p..

        w___ stack:
            res.append(stack.pop())

        r_ res

    ___ eval_rpn(self, s
        stack =   # list

        ___ char __ s:
            __ char.isdigit(
                stack.append(int(char))
            ____ char __ self.OP:
                b = stack.p..
                a = stack.p..
                stack.append(self.OP[char](a, b))

        r_ stack[0]


class Solution:
    ___ calculate(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ 0

        s = self.to_rpn(s)

        __ not s:
            r_ 0

        r_ self.eval_rpn(s)

    ___ to_rpn(self, s
        stack, res =   # list, []

        ___ i __ range(le.(s)):
            char = s[i]

            __ i > 0 and s[i - 1].isdigit() and char.isdigit(
                res[-1] += char
            ____ char.isdigit(
                res.append(char)
            ____ char __ '+-':
                w___ stack and stack[-1] __ '+-':
                    res.append(stack.pop())
                stack.append(char)
            ____ char __ '(':
                stack.append(char)
            ____ char __ ')':
                w___ stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.p..

        w___ stack:
            res.append(stack.pop())

        r_ res

    ___ eval_rpn(self, s
        stack =   # list

        ___ char __ s:
            __ char.isdigit(
                stack.append(int(char))
            ____ char __ '+-':
                b = stack.p..
                a = stack.p..

                __ char __ '+':
                    stack.append(a + b)
                ____ char __ '-':
                    stack.append(a - b)

        r_ stack[0]
