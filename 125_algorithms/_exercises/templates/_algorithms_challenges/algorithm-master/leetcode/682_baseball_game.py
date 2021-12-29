class Solution:
    ___ calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        __ not ops:
            return 0

        stack = []

        for op in ops:
            __ op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)
