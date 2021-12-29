class Solution:
    """
    @param: A: a list of n integers
    @return: true if there is a 132 pattern or false
    """
    ___ find132pattern(self, A):
        __ n.. A:
            r.. False

        stack = [float('-inf')]
        ___ i __ r..(l..(A) - 1, -1, -1):
            __ A[i] < stack[-1]:
                r.. True

            v = N..
            while stack and A[i] > stack[-1]:
                v = stack.pop()

            stack.a..(A[i])

            __ v __ n.. N..
                stack.a..(v)

        r.. False
