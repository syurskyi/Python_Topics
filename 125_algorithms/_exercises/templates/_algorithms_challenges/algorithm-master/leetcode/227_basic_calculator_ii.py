class Solution:
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. 0

        s = self.to_rpn(s, {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        })

        __ n.. s:
            r.. 0

        r.. self.eval_rpn(s, {
            '+': l.... a, b: a + b,
            '-': l.... a, b: a - b,
            '*': l.... a, b: a * b,
            '/': l.... a, b: a // b,
        })

    ___ to_rpn(self, s, P):
        stack, res    # list, []

        ___ i __ r..(l..(s)):
            char = s[i]

            __ i > 0 and s[i - 1].isdigit() and char.isdigit():
                res[-1] += char
            ____ char.isdigit():
                res.a..(char)
            ____ char __ P:
                while stack and stack[-1] __ P and P[char] <= P[stack[-1]]:
                    res.a..(stack.pop())
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                while stack and stack[-1] != '(':
                    res.a..(stack.pop())
                stack.pop()

        while stack:
            res.a..(stack.pop())

        r.. res

    ___ eval_rpn(self, s, OP):
        stack    # list

        ___ char __ s:
            __ char.isdigit():
                stack.a..(int(char))
            ____ char __ OP:
                b = stack.pop()
                a = stack.pop()
                stack.a..(OP[char](a, b))

        r.. stack[0]


class Solution:
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. 0

        s = self.to_rpn(s)

        __ n.. s:
            r.. 0

        r.. self.eval_rpn(s)

    ___ to_rpn(self, s):
        stack, res    # list, []

        ___ i __ r..(l..(s)):
            char = s[i]

            __ i > 0 and s[i - 1].isdigit() and char.isdigit():
                res[-1] += char
            ____ char.isdigit():
                res.a..(char)
            ____ char __ '+-*/':
                while stack and stack[-1] __ '+-*/':
                    __ char __ '*/' and stack[-1] __ '+-':
                        break
                    res.a..(stack.pop())
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                while stack and stack[-1] != '(':
                    res.a..(stack.pop())
                stack.pop()

        while stack:
            res.a..(stack.pop())

        r.. res

    ___ eval_rpn(self, s):
        stack    # list

        ___ char __ s:
            __ char.isdigit():
                stack.a..(int(char))
            ____ char __ '+-*/':
                b = stack.pop()
                a = stack.pop()

                __ char __ '+':
                    stack.a..(a + b)
                ____ char __ '-':
                    stack.a..(a - b)
                ____ char __ '*':
                    stack.a..(a * b)
                ____ char __ '/':
                    stack.a..(a // b)

        r.. stack[0]
