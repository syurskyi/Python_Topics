c_ Solution:
    # @param A a list of integers
    # @return an integer
    ___ removeDuplicates  A
        __ n.. A:
            r.. 0
        j 0
        counter 0  # How many times repeated (1 for twice)
        n l..(A)
        ___ i __ r..(1, n
            __ A[i] __ A[j] a.. counter <_ 0:
                j += 1
                A[j] A[i]
                counter += 1
            ____ A[i] !_ A[j]:
                j += 1
                A[j] A[i]
                counter 0
        r.. j + 1
