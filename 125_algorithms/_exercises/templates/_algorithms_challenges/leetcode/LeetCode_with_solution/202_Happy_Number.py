c_ Solution o..
    ___ isHappy  n
        """
        :type n: int
        :rtype: bool
        """
        # https://en.wikipedia.org/wiki/Happy_number
        seen_numbers = s..()
        w.. n > 1 and n n.. __ seen_numbers:
            seen_numbers.add(n)
            n = s..(map(lambda x: i..(x) * i..(x), list(s..(n))))
        r_ n __ 1