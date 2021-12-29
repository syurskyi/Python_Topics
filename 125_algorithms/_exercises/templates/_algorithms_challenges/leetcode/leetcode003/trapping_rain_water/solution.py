class Solution:
    # @param A, a list of integers
    # @return an integer
    ___ trap(self, A):
        n = l..(A)
        res = 0
        last = 0
        stack    # list
        ___ i __ r..(1, n):
            __ A[i] >= A[last]:
                # Calculate trapped water
                w = i - last - 1
                area = w * A[last]
                w.... stack:
                    area -= A[stack.pop()]
                res += area
                last = i
            ____:
                stack.a..(i)
        # Process remaining bars
        __ stack:
            r = stack.pop()  # Rightmost effective bar
            w.... stack:
                __ A[stack[-1]] >= A[r]:
                    r = stack.pop()
                ____:
                    break
            w.... stack:
                i = stack.pop()
                __ A[i] < A[r]:
                    res += A[r] - A[i]
                ____:
                    r = i
        r.. res
