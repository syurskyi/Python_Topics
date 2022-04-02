c_ Solution:
    """
    @param: x: An integer
    @return: An integer
    """
    ___ swapOddEvenBits  x
        """
        0x55555555 == 01010101010101010101010101010101 (2)
        0xAAAAAAAA == 10101010101010101010101010101010 (2)
        """
        r.. ( ((x & 0xAAAAAAAA) >> 1) | ((x & 0x55555555) << 1) )
