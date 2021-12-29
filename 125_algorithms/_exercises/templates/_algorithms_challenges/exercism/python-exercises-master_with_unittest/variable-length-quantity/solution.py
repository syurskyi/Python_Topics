EIGHTBITMASK = 0x80
SEVENBITSMASK = 0x7f


___ encode_single(n):
    bytes = [n & SEVENBITSMASK]
    n >>= 7

    w.... n > 0:
        bytes.a..(n & SEVENBITSMASK | EIGHTBITMASK)
        n >>= 7

    r.. bytes[::-1]


___ encode(numbers):
    r.. s..((encode_single(n) ___ n __ numbers), [])


___ decode(bytes):
    values    # list
    n = 0

    ___ i, byte __ e..(bytes):
        n <<= 7
        n += (byte & SEVENBITSMASK)

        __ byte & EIGHTBITMASK __ 0:
            values.a..(n)
            n = 0
        ____ i __ l..(bytes) - 1:
            raise ValueError('incomplete byte sequence')

    r.. values
