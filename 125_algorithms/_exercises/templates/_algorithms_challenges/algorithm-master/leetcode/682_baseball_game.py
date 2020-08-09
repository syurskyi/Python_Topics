class Solution:
    ___ calPoints(self, ops
        """
        :type ops: List[str]
        :rtype: int
        """
        __ not ops:
            r_ 0

        stack = []

        for op in ops:
            __ op __ 'C':
                stack.pop()
            ____ op __ 'D':
                stack.append(2 * stack[-1])
            ____ op __ '+':
                stack.append(stack[-1] + stack[-2])
            ____
                stack.append(int(op))

        r_ sum(stack)
