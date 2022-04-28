c_ Solution o..
    ___ isHappy  n):
        """
        :type n: int
        :rtype: bool
        """
        # https://en.wikipedia.org/wiki/Happy_number
        seen_numbers = set()
        w.. n > 1 and n not __ seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        r_ n __ 1