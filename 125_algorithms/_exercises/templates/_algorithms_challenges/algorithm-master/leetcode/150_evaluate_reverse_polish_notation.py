class Solution:
    ___ evalRPN(self, E):
        """
        :type E: List[str]
        :rtype: int
        """
        __ n.. E:
            r.. 0

        stack    # list
        operation = {
            '+': l.... a, b: a + b,
            '-': l.... a, b: a - b,
            '*': l.... a, b: a * b,
            '/': l.... a, b: a / b,
        }

        ___ char __ E:
            __ char n.. __ operation:
                stack.a..(int(char))
                continue

            b = stack.pop()
            a = stack.pop()

            stack.a..(int(operation[char](a, b)))

        r.. stack[0]
