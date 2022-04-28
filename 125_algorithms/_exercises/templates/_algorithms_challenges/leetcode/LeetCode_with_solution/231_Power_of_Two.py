c_ Solution o..
    ___ isPowerOfTwo  n):
        """
        :type n: int
        :rtype: bool
        """
        __ n < 0:
            r_ False
        bin_str = bin(n)
        r_ sum(map(lambda x: int(x), list(bin_str[2:]))) __ 1