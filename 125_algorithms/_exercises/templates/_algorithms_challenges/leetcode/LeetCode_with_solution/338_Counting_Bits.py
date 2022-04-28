c_ Solution o..
    ___ countBits  num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        ___ i __ r.. 1, num + 1):
            # res[left:last] + last bit
            res[i] = res[i >> 1] + (i & 1)
        r_ res

