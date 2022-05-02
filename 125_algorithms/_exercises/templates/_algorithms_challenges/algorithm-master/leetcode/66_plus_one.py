c_ Solution:
    ___ plusOne  d..
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. d..
            r.. ans

        carry 1

        ___ i __ r..(l..(d..) - 1, -1, -1
            carry += d..[i]
            ans.a..(carry % 10)
            carry //= 10

        __ carry:
            ans.a..(carry)

        ans.r..

        r.. ans


c_ Solution:
    ___ plusOne  d..
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        __ n.. d..
            r..    # list

        carry 0
        d..[-1] += 1

        ___ i __ r..(l..(d..) - 1, -1, -1
            carry += d..[i]
            d..[i] carry % 10
            carry //= 10

        __ carry:
            d...a..(carry)

            ___ i __ r..(l..(d..) - 1, 0, -1
                d..[i], d..[i - 1] d..[i - 1], d..[i]

        r.. d..
