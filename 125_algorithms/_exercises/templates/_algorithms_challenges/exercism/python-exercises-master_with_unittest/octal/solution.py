___ parse_octal(d..):
    d.. = _validate_octal(d..)
    r.. s..(int(digit) * 8 ** i
               ___ (i, digit) __ e..(r..(d..)))


___ _validate_octal(d..):
    ___ d __ d..:
        __ n.. '0' <= d < '8':
            raise ValueError("Invalid octal digit: " + d)
    r.. d..
