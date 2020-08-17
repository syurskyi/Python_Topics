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
    ___ evaluateExpression(self, E
        __ not E:
            r_ 0

        E = self.dal2rpn(E)

        """
        for cases like `["(","(","(","(","(",")",")",")",")",")"]`
        """
        __ not E:
            r_ 0

        r_ self.eval_rpn(E)

    ___ dal2rpn(self, E
        """
        `stack` to save operators and brackets temply
        `res` is the RPN of `E`, to save digits and operators
        """
        stack, res = [], []

        ___ char in E:
            __ char.isdigit(
                """
                if its digit
                then directly output
                """
                res.append(char)
                continue

            __ char in self.P:
                """
                if `stack` is not empty
                and `stack[-1]` is an operator
                and its priority is higher or same ('*' == '/' > '+' == '-')
                then pop and output
                """
                w___ (stack and stack[-1] in self.P and
                       self.P[stack[-1]] >= self.P[char]
                    res.append(stack.pop())
                stack.append(char)
            ____ char __ '(':
                stack.append(char)
            ____ char __ ')':
                """
                if its ')'
                then continue to pop and output
                until meet '('
                """
                w___ stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.p..  # evict '('

        """
        output the remaining in `stack`
        """
        w___ stack:
            res.append(stack.pop())

        r_ res

    ___ eval_rpn(self, E
        stack = []
        ___ char in E:
            __ char.isdigit(
                """
                if its digit
                then temply save in `stack`
                """
                stack.append(int(char))
                continue

            """
            the first poped one is base,
            otherwise there is error occurred when '/' and '-'
            """
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
