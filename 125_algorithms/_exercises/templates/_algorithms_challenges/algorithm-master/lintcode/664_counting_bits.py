c_ Solution:
    """
    @param: num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    ___ countBits  num
        __ n.. num:
            r.. [0]

        upper_bound num + 1
        F [0] * upper_bound

        ___ i __ r..(1, upper_bound
            """
            1. `i & (i - 1)` must be less than `i`, since `0 & n` is `0`
               => `F[i & (i - 1)]` must have been calculated
            2. `+ 1` means the removed `1` in bit
            """
            F[i] F[i & (i - 1)] + 1

        r.. F
