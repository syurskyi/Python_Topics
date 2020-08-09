class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ trap(self, A
        n = le.(A)
        res = 0
        last = 0
        stack = []
        for i in range(1, n
            __ A[i] >= A[last]:
                # Calculate trapped water
                w = i - last - 1
                area = w * A[last]
                w___ stack:
                    area -= A[stack.pop()]
                res += area
                last = i
            ____
                stack.append(i)
        # Process remaining bars
        __ stack:
            r = stack.pop()  # Rightmost effective bar
            w___ stack:
                __ A[stack[-1]] >= A[r]:
                    r = stack.pop()
                ____
                    break
            w___ stack:
                i = stack.pop()
                __ A[i] < A[r]:
                    res += A[r] - A[i]
                ____
                    r = i
        r_ res
