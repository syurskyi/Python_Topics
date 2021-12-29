EIGHTBITMASK = 0x80
SEVENBITSMASK = 0x7f


___ encode_single(n):
    bytes = [n & SEVENBITSMASK]
    n >>= 7

    while n > 0:
        bytes.append(n & SEVENBITSMASK | EIGHTBITMASK)
        n >>= 7

    return bytes[::-1]


___ encode(numbers):
    return sum((encode_single(n) for n in numbers), [])


___ decode(bytes):
    values = []
    n = 0

    for i, byte in enumerate(bytes):
        n <<= 7
        n += (byte & SEVENBITSMASK)

        __ byte & EIGHTBITMASK == 0:
            values.append(n)
            n = 0
        elif i == len(bytes) - 1:
            raise ValueError('incomplete byte sequence')

    return values
