EIGHTBITMASK = 0x80
SEVENBITSMASK = 0x7f


___ encode_single(n
    bytes = [n & SEVENBITSMASK]
    n >>= 7

    w___ n > 0:
        bytes.append(n & SEVENBITSMASK | EIGHTBITMASK)
        n >>= 7

    r_ bytes[::-1]


___ encode(numbers
    r_ su.((encode_single(n) ___ n __ numbers),   # list)


___ decode(bytes
    values =   # list
    n = 0

    ___ i, byte __ enumerate(bytes
        n <<= 7
        n += (byte & SEVENBITSMASK)

        __ byte & EIGHTBITMASK __ 0:
            values.append(n)
            n = 0
        ____ i __ le.(bytes) - 1:
            raise ValueError('incomplete byte sequence')

    r_ values
