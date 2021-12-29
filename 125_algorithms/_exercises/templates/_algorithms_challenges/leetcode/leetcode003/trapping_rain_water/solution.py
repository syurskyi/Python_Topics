class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ trap(self, A):
        n = len(A)
        res = 0
        last = 0
        stack = []
        for i in range(1, n):
            __ A[i] >= A[last]:
                # Calculate trapped water
                w = i - last - 1
                area = w * A[last]
                while stack:
                    area -= A[stack.pop()]
                res += area
                last = i
            else:
                stack.append(i)
        # Process remaining bars
        __ stack:
            r = stack.pop()  # Rightmost effective bar
            while stack:
                __ A[stack[-1]] >= A[r]:
                    r = stack.pop()
                else:
                    break
            while stack:
                i = stack.pop()
                __ A[i] < A[r]:
                    res += A[r] - A[i]
                else:
                    r = i
        return res
