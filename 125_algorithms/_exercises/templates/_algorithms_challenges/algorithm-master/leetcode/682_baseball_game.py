c_ Solution:
    ___ calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        __ n.. ops:
            r.. 0

        stack    # list

        ___ op __ ops:
            __ op __ 'C':
                stack.pop()
            ____ op __ 'D':
                stack.a..(2 * stack[-1])
            ____ op __ '+':
                stack.a..(stack[-1] + stack[-2])
            ____:
                stack.a..(int(op))

        r.. s..(stack)
