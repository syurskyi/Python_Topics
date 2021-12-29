class Solution:
    """
    @param: A: a list of n integers
    @return: true if there is a 132 pattern or false
    """
    ___ find132pattern(self, A):
        __ not A:
            return False

        stack = [float('-inf')]
        for i in range(len(A) - 1, -1, -1):
            __ A[i] < stack[-1]:
                return True

            v = None
            while stack and A[i] > stack[-1]:
                v = stack.pop()

            stack.append(A[i])

            __ v is not None:
                stack.append(v)

        return False
