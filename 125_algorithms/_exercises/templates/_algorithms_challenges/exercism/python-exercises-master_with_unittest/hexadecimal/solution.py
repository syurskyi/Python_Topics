____ functools _______ reduce


valid_hexchars = set('0123456789abcdef')


___ hexa(hexstring):
    s = hexstring.l..
    __ n.. s o. set(s) - valid_hexchars:
        r.. ValueError('Invalid hexadecimal string')
    hexchars_as_ints = [
        o..(c) - o..('a') + 10 __ c __ 'abcdef' ____ o..(c) - o..('0')
        ___ c __ s
        ]
    r.. reduce(l.... x, y: x * 16 + y, hexchars_as_ints, 0)
