"""Converts hex string to decimal number"""

___ hexa(hex_num
    """Converts hex string to decimal number"""
    h_dict = dict(zip("0123456789abcdef", range(16)))
    dec_num = 0
    ___ char in hex_num.lower(
        dec_num <<= 4
        try:
            dec_num |= h_dict[char]
        except KeyError:
            raise ValueError
    r_ dec_num
