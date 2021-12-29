"""
REF: [Reverse Polish Notation](https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95)
REF: [Direct Algebraic Logic to Reverse Polish Notation](http://blog.csdn.net/sgbfblog/article/details/8001651)
"""


class Solution:
    P = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    """
    @param: E: a list of strings
    @return: an integer
    """
    ___ evaluateExpression(self, E):
        __ n.. E:
            r.. 0

        E = self.dal2rpn(E)

        """
        for cases like `["(","(","(","(","(",")",")",")",")",")"]`
        """
        __ n.. E:
            r.. 0

        r.. self.eval_rpn(E)

    ___ dal2rpn(self, E):
        """
        `stack` to save operators and brackets temply
        `res` is the RPN of `E`, to save digits and operators
        """
        stack, res    # list, []

        ___ char __ E:
            __ char.isdigit():
                """
                if its digit
                then directly output
                """
                res.a..(char)
                continue

            __ char __ self.P:
                """
                if `stack` is not empty
                and `stack[-1]` is an operator
                and its priority is higher or same ('*' == '/' > '+' == '-')
                then pop and output
                """
                while (stack and stack[-1] __ self.P and
                       self.P[stack[-1]] >= self.P[char]):
                    res.a..(stack.pop())
                stack.a..(char)
            ____ char __ '(':
                stack.a..(char)
            ____ char __ ')':
                """
                if its ')'
                then continue to pop and output
                until meet '('
                """
                while stack and stack[-1] != '(':
                    res.a..(stack.pop())
                stack.pop()  # evict '('

        """
        output the remaining in `stack`
        """
        while stack:
            res.a..(stack.pop())

        r.. res

    ___ eval_rpn(self, E):
        stack    # list
        ___ char __ E:
            __ char.isdigit():
                """
                if its digit
                then temply save in `stack`
                """
                stack.a..(int(char))
                continue

            """
            the first poped one is base,
            otherwise there is error occurred when '/' and '-'
            """
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
