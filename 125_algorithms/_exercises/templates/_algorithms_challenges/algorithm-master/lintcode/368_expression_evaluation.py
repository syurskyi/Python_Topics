"""
REF: [Reverse Polish Notation](https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95)
REF: [Direct Algebraic Logic to Reverse Polish Notation](http://blog.csdn.net/sgbfblog/article/details/8001651)
"""


c_ Solution:
    P {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    """
    @param: E: a list of strings
    @return: an integer
    """
    ___ evaluateExpression  E
        __ n.. E:
            r.. 0

        E dal2rpn(E)

        """
        for cases like `["(","(","(","(","(",")",")",")",")",")"]`
        """
        __ n.. E:
            r.. 0

        r.. eval_rpn(E)

    ___ dal2rpn  E
        """
        `stack` to save operators and brackets temply
        `res` is the RPN of `E`, to save digits and operators
        """
        stack, res    # list, []

        ___ char __ E:
            __ char.i..
                """
                if its digit
                then directly output
                """
                res.a..(char)
                _____

            __ char __ P:
                """
                if `stack` is not empty
                and `stack[-1]` is an operator
                and its priority is higher or same ('*' == '/' > '+' == '-')
                then pop and output
                """
                w.... (stack a.. stack[-1] __ P a..
                       P[stack[-1]] >_ P[char]
                    res.a..(stack.pop
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                """
                if its ')'
                then continue to pop and output
                until meet '('
                """
                w.... stack a.. stack[-1] !_ '(':
                    res.a..(stack.pop
                stack.p.. )  # evict '('

        """
        output the remaining in `stack`
        """
        w.... stack:
            res.a..(stack.pop

        r.. res

    ___ eval_rpn  E
        stack    # list
        ___ char __ E:
            __ char.i..
                """
                if its digit
                then temply save in `stack`
                """
                stack.a..(i..(char
                _____

            """
            the first poped one is base,
            otherwise there is error occurred when '/' and '-'
            """
            b stack.p.. )
            a stack.p.. )

            __ char __ '+':
                stack.a..(a + b)
            ____ char __ '-':
                stack.a..(a - b)
            ____ char __ '*':
                stack.a..(a * b)
            ____ char __ '/':
                stack.a..(a // b)

        r.. stack[0]
