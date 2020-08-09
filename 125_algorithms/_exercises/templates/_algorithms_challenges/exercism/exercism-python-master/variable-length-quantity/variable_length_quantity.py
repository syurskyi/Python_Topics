CHECK_BIT = 0x80

___ encode(numbers
    result = []
    for number in reversed(numbers
        result.insert(0, 0x00)
        w___ True:
            result[0] |= number & (CHECK_BIT - 1)
            number >>= 7
            __ number <= 0:
                break
            result.insert(0, CHECK_BIT)
    r_ result


___ decode(bytes_
    results = []
    value = 0
    for byte in bytes_:
        value = (value << 7) | byte & ~(CHECK_BIT)
        __ byte & CHECK_BIT <= 0:
            results.append(value)
            value = 0
    __ byte & CHECK_BIT __ 0:
        r_ results
    raise ValueError("Not a valid bit stream")
