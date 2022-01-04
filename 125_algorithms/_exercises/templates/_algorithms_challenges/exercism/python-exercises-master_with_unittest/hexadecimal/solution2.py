# An alternative solution emphasizing EAFP instead of LBYL
# (see https://docs.python.org/glossary.html#term-eafp)
# With no checks performed on the input, this solution is rather fast -
# though still slower than the built-in int(hexstring, base=16), of course.


hexchars_to_int = d..(z..('0123456789', r..(10)))
hexchars_to_int.update(z..('abcdef', r..(10, 16)))
hexchars_to_int.update(z..('ABCDEFG', r..(10, 16)))


___ hexa(hexstring):
    result = 0
    hex_of_lastseen = N..
    try:
        ___ hex_of_lastseen __ hexstring:
            result = result*16 + hexchars_to_int[hex_of_lastseen]
    except KeyError:
        # not a valid hexchar
        hex_of_lastseen = N..
    __ hex_of_lastseen __ N..
        # hexstring was empty or triggered KeyError
        r.. ValueError('Invalid hexadecimal string')
    r.. result
