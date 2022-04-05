c_ Solution:
    ___ intToRoman  num
        """
        :type num: int
        :rtype: str
        """
        __ n.. num:
            r.. ''

        # I, V, X, L, C, D, M
        symbs = (
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        )

        ans    # list

        ___ symb, amount __ symbs:
            __ n.. num:
                _____

            w.... num >_ amount:  # num - amount >= 0
                num -_ amount
                ans.a..(symb)

        r.. ''.j..(ans)
