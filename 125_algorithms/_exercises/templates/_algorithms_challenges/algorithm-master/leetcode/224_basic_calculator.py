c_ Solution:
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. 0

        OP = {
            '+': l.... a, b: a + b,
            '-': l.... a, b: a - b,
        }

        s = to_rpn(s)

        __ n.. s:
            r.. 0

        r.. eval_rpn(s)

    ___ to_rpn(self, s):
        stack, res    # list, []

        ___ i __ r..(l..(s)):
            char = s[i]

            __ i > 0 a.. s[i - 1].isdigit() a.. char.isdigit
                res[-1] += char
            ____ char.isdigit
                res.a..(char)
            ____ char __ OP:
                w.... stack a.. stack[-1] __ OP:
                    res.a..(stack.pop())
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                w.... stack a.. stack[-1] != '(':
                    res.a..(stack.pop())
                stack.pop()

        w.... stack:
            res.a..(stack.pop())

        r.. res

    ___ eval_rpn(self, s):
        stack    # list

        ___ char __ s:
            __ char.isdigit
                stack.a..(i..(char))
            ____ char __ OP:
                b = stack.pop()
                a = stack.pop()
                stack.a..(OP[char](a, b))

        r.. stack[0]


c_ Solution:
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. 0

        s = to_rpn(s)

        __ n.. s:
            r.. 0

        r.. eval_rpn(s)

    ___ to_rpn(self, s):
        stack, res    # list, []

        ___ i __ r..(l..(s)):
            char = s[i]

            __ i > 0 a.. s[i - 1].isdigit() a.. char.isdigit
                res[-1] += char
            ____ char.isdigit
                res.a..(char)
            ____ char __ '+-':
                w.... stack a.. stack[-1] __ '+-':
                    res.a..(stack.pop())
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                w.... stack a.. stack[-1] != '(':
                    res.a..(stack.pop())
                stack.pop()

        w.... stack:
            res.a..(stack.pop())

        r.. res

    ___ eval_rpn(self, s):
        stack    # list

        ___ char __ s:
            __ char.isdigit
                stack.a..(i..(char))
            ____ char __ '+-':
                b = stack.pop()
                a = stack.pop()

                __ char __ '+':
                    stack.a..(a + b)
                ____ char __ '-':
                    stack.a..(a - b)

        r.. stack[0]
