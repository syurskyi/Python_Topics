from functools ______ reduce


valid_hexchars = set('0123456789abcdef')


___ hexa(hexstring
    s = hexstring.lower()
    __ not s or set(s) - valid_hexchars:
        raise ValueError('Invalid hexadecimal string')
    hexchars_as_ints = [
        ord(c) - ord('a') + 10 __ c in 'abcdef' else ord(c) - ord('0')
        for c in s
        ]
    r_ reduce(lambda x, y: x * 16 + y, hexchars_as_ints, 0)
