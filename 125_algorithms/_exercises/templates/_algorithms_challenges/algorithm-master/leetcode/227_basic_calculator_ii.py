class Solution:
    ___ calculate(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ 0

        s = self.to_rpn(s, {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        })

        __ not s:
            r_ 0

        r_ self.eval_rpn(s, {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b,
        })

    ___ to_rpn(self, s, P
        stack, res = [], []

        ___ i in range(le.(s)):
            char = s[i]

            __ i > 0 and s[i - 1].isdigit() and char.isdigit(
                res[-1] += char
            ____ char.isdigit(
                res.append(char)
            ____ char in P:
                w___ stack and stack[-1] in P and P[char] <= P[stack[-1]]:
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

    ___ eval_rpn(self, s, OP
        stack = []

        ___ char in s:
            __ char.isdigit(
                stack.append(int(char))
            ____ char in OP:
                b = stack.p..
                a = stack.p..
                stack.append(OP[char](a, b))

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
        stack, res = [], []

        ___ i in range(le.(s)):
            char = s[i]

            __ i > 0 and s[i - 1].isdigit() and char.isdigit(
                res[-1] += char
            ____ char.isdigit(
                res.append(char)
            ____ char in '+-*/':
                w___ stack and stack[-1] in '+-*/':
                    __ char in '*/' and stack[-1] in '+-':
                        break
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
        stack = []

        ___ char in s:
            __ char.isdigit(
                stack.append(int(char))
            ____ char in '+-*/':
                b = stack.p..
                a = stack.p..

                __ char __ '+':
                    stack.append(a + b)
                ____ char __ '-':
                    stack.append(a - b)
                ____ char __ '*':
                    stack.append(a * b)
                ____ char __ '/':
                    stack.append(a // b)

        r_ stack[0]
