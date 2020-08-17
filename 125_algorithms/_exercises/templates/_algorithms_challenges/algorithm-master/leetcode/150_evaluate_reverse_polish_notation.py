class Solution:
    ___ evalRPN(self, E
        """
        :type E: List[str]
        :rtype: int
        """
        __ not E:
            r_ 0

        stack = []
        operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

        ___ char in E:
            __ char not in operation:
                stack.append(int(char))
                continue

            b = stack.p..
            a = stack.p..

            stack.append(int(operation[char](a, b)))

        r_ stack[0]
