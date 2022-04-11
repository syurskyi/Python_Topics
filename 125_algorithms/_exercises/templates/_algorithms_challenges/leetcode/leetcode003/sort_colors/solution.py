c_ Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    ___ sortColors  A
        n l..(A)
        r 0  # Last index of red
        b n - 1  # First index of white
        i 0
        w.... i <_ b:
            __ A[i] __ 0:
                A[i], A[r] A[r], A[i]
                r += 1
                # Increment i because swapped item must be 1 or 0
                i += 1
            ____ A[i] __ 2:
                A[i], A[b] A[b], A[i]
                b -_ 1
                # Do not increment i, since swapped item may be 0, 1, or 2
                _____
            # A[i] == 1
            ____
                i += 1
