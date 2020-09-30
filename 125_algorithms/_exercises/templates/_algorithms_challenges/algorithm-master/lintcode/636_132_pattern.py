class Solution:
    """
    @param: A: a list of n integers
    @return: true if there is a 132 pattern or false
    """
    ___ find132pattern(self, A
        __ not A:
            r_ False

        stack = [float('-inf')]
        ___ i __ range(le.(A) - 1, -1, -1
            __ A[i] < stack[-1]:
                r_ True

            v = None
            w___ stack and A[i] > stack[-1]:
                v = stack.p..

            stack.append(A[i])

            __ v pa__ not None:
                stack.append(v)

        r_ False
