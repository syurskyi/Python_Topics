class Solution:
    """
    @param: num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    ___ countBits(self, num
        __ not num:
            r_ [0]

        upper_bound = num + 1
        F = [0] * upper_bound

        for i in range(1, upper_bound
            """
            1. `i & (i - 1)` must be less than `i`, since `0 & n` is `0`
               => `F[i & (i - 1)]` must have been calculated
            2. `+ 1` means the removed `1` in bit
            """
            F[i] = F[i & (i - 1)] + 1

        r_ F
