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
    r_ sum((encode_single(n) for n in numbers), [])


___ decode(bytes
    values = []
    n = 0

    for i, byte in enumerate(bytes
        n <<= 7
        n += (byte & SEVENBITSMASK)

        __ byte & EIGHTBITMASK __ 0:
            values.append(n)
            n = 0
        ____ i __ le.(bytes) - 1:
            raise ValueError('incomplete byte sequence')

    r_ values
