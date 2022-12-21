c_ Solution o..
    ___ addDigits  num
        """
        :type num: int
        :rtype: int
        """
        # https: // en.wikipedia.org / wiki / Digital_root
        __ num < 10:
            r_ num
        r_ num - ((num - 1) / 9) * 9