c_ Solution:
    # @param A, a list of integers
    # @return an integer
    ___ trap  A
        n = l..(A)
        res = 0
        last = 0
        stack    # list
        ___ i __ r..(1, n
            __ A[i] >_ A[last]:
                # Calculate trapped water
                w = i - last - 1
                area = w * A[last]
                w.... stack:
                    area -_ A[stack.p.. )]
                res += area
                last = i
            ____
                stack.a..(i)
        # Process remaining bars
        __ stack:
            r = stack.p.. )  # Rightmost effective bar
            w.... stack:
                __ A[stack[-1]] >_ A[r]:
                    r = stack.p.. )
                ____
                    _____
            w.... stack:
                i = stack.p.. )
                __ A[i] < A[r]:
                    res += A[r] - A[i]
                ____
                    r = i
        r.. res
