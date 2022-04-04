c_ Solution:
    ___ calculate  s
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

    ___ to_rpn  s
        stack, res    # list, []

        ___ i __ r..(l..(s:
            char = s[i]

            __ i > 0 a.. s[i - 1].i.. a.. char.i..
                res[-1] += char
            ____ char.i..
                res.a..(char)
            ____ char __ OP:
                w.... stack a.. stack[-1] __ OP:
                    res.a..(stack.pop
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                w.... stack a.. stack[-1] != '(':
                    res.a..(stack.pop
                stack.p.. )

        w.... stack:
            res.a..(stack.pop

        r.. res

    ___ eval_rpn  s
        stack    # list

        ___ char __ s:
            __ char.i..
                stack.a..(i..(char
            ____ char __ OP:
                b = stack.p.. )
                a = stack.p.. )
                stack.a..(OP[char](a, b

        r.. stack[0]


c_ Solution:
    ___ calculate  s
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

    ___ to_rpn  s
        stack, res    # list, []

        ___ i __ r..(l..(s:
            char = s[i]

            __ i > 0 a.. s[i - 1].i.. a.. char.i..
                res[-1] += char
            ____ char.i..
                res.a..(char)
            ____ char __ '+-':
                w.... stack a.. stack[-1] __ '+-':
                    res.a..(stack.pop
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                w.... stack a.. stack[-1] != '(':
                    res.a..(stack.pop
                stack.p.. )

        w.... stack:
            res.a..(stack.pop

        r.. res

    ___ eval_rpn  s
        stack    # list

        ___ char __ s:
            __ char.i..
                stack.a..(i..(char
            ____ char __ '+-':
                b = stack.p.. )
                a = stack.p.. )

                __ char __ '+':
                    stack.a..(a + b)
                ____ char __ '-':
                    stack.a..(a - b)

        r.. stack[0]
