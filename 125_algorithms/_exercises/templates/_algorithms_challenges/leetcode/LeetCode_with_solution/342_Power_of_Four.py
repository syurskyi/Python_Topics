c_ Solution o..
    ___ isPowerOfFour  num
        """
        :type num: int
        :rtype: bool
        """
        # bin(4**0) '0b1'
        # bin(4**1) '0b100'
        # bin(4**2) '0b10000'
        # bin(4**3) '0b1000000'
        r_ num > 0 a.. num & (num-1) __ 0 a.. l.. bin(num)[3:]) % 2 __ 0