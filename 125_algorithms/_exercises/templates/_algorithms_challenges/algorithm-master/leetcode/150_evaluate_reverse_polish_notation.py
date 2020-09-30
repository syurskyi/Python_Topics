class Solution:
    ___ evalRPN(self, E
        """
        :type E: List[str]
        :rtype: int
        """
        __ not E:
            r_ 0

        stack =   # list
        operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

        ___ char __ E:
            __ char not __ operation:
                stack.append(int(char))
                continue

            b = stack.p..
            a = stack.p..

            stack.append(int(operation[char](a, b)))

        r_ stack[0]
