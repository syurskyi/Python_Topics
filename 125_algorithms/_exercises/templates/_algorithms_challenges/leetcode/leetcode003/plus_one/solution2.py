c_ Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne  d..
        # In-place version
        d...r..
        d = d..[0]
        d..[0] = (d + 1) % 10
        carry = (d + 1) / 10
        ___ i, d __ e..(d..[1:], 1
            d..[i] = (d + carry) % 10
            carry = (d + carry) / 10
        __ carry __ 1:
            d...a..(1)
        d...r..
        r.. d..
