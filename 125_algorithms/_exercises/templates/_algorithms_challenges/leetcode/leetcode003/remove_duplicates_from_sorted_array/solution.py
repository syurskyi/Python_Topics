c_ Solution:
    # @param a list of integers
    # @return an integer
    ___ removeDuplicates  A):
        __ n.. A:
            r.. 0
        __ l..(A) __ 1:
            r.. 1
        j = 0  # Position of last processed non-duplicate
        n = l..(A)
        ___ i __ r..(1, n):
            __ A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1
        r.. j + 1
